"""Independent QM calculation for the Kim et al. (2000) delayed-choice eraser,
compared with Campbell et al. (2017) Eq. (2).
Signal photon at D0 (Fourier plane of lens f): amplitude from region A / B.
Idler: mode a (from A) or b (from B).
  BSA (reflectance rA to which-path det D3, transmittance 1-rA towards BS)
  BSB (reflectance rB to D4, 1-rB towards BS)
  BS  (transmittance t): D1 <- sqrt(t) a' + sqrt(1-t) b',  D2 <- sqrt(1-t) a' - sqrt(t) b'
Detector efficiencies eta1..eta4. R=1 := which-path (D3 or D4), R=0 := erasure (D1 or D2).
(Kim's text routes transmission->D3/D4 and reflection->BS; the labels are immaterial.)
"""
import numpy as np
lam, f, d, aslit = 702.2e-9, 1.0, 0.7e-3, 0.3e-3   # Kim et al. numbers; f arbitrary
period = lam*f/d
x = np.linspace(-2*period, 2*period, 4001)
env = np.sinc(aslit*x/(lam*f))          # np.sinc(u)=sin(pi u)/(pi u)
psiA = env*np.exp(+1j*np.pi*d*x/(lam*f))/np.sqrt(2)
psiB = env*np.exp(-1j*np.pi*d*x/(lam*f))/np.sqrt(2)

def joint(rA=.5, rB=.5, t=.5, eta=(1,1,1,1), phi=0.0):
    e1,e2,e3,e4 = eta
    tA, tB = np.sqrt(1-rA), np.sqrt(1-rB)
    # amplitudes (phi = interferometer phase between arms A and B before BS)
    A1 = np.sqrt(t)*tA*psiA + np.sqrt(1-t)*tB*np.exp(1j*phi)*psiB
    A2 = np.sqrt(1-t)*tA*psiA - np.sqrt(t)*tB*np.exp(1j*phi)*psiB
    A3 = np.sqrt(rA)*psiA
    A4 = np.sqrt(rB)*psiB
    P = [e1*abs(A1)**2, e2*abs(A2)**2, e3*abs(A3)**2, e4*abs(A4)**2]
    return P

def report(label, **kw):
    P1,P2,P3,P4 = joint(**kw)
    tot = P1+P2+P3+P4
    pR1 = (P3+P4)/tot
    marg = tot
    V = lambda y: (y.max()-y.min())/(y.max()+y.min())
    core = abs(x) < 0.5*period*1.01   # central period, envelope ~1
    print(f"{label:48s} P(R=1|x): min {pR1[core].min():.4f} max {pR1[core].max():.4f} | "
          f"V(D0 marginal, central) {V(marg[core]):.4f} | V(R01) {V(P1[core]):.3f} V(R02) {V(P2[core]):.3f} V(R01+R02) {V((P1+P2)[core]):.4f}")

report("ideal Kim (50:50 BSA/BSB/BS, eta=1)")
report("BS 70:30 (erasing BS unbalanced)", t=0.7)
report("BSA 0.5, BSB 0.4 (unequal)", rA=.5, rB=.4)
report("eta1=0.9, eta2=0.6 (unequal erasing dets)", eta=(0.9,0.6,1,1))
report("eta1=0.9, eta2=0.6, BS 70:30", eta=(0.9,0.6,1,1), t=0.7)
report("interferometer phase pi/3", phi=np.pi/3)
report("only D1 counted (D2 removed, eta2=0)", eta=(1,0,1,1))

# Campbell Eq.(2)
c = np.cos(np.pi*x/period)**2
PC = 1/(1+2*c)
print("\nCampbell Eq.(2): at bright fringe (cos^2=1):", 1/3, " at dark fringe:", 1.0)
print("max |Eq.(2) - 1/2| =", np.max(abs(PC-0.5)), " at bright fringe |1/3-1/2| =", 1/6)
# Implied D0 marginal under Campbell's assumptions: P(x) = 1/2*(4I0cos^2) + 1/2*(2I0) = I0(1+2cos^2)
m = 1+2*c
print("Implied unconditioned D0 visibility under Campbell's assumptions:", (m.max()-m.min())/(m.max()+m.min()))
# consistency: E[P(R=1|X)] under Campbell's own marginal
w = m/m.mean()
print("E_X[P(R=1|X)] under Campbell's marginal:", np.mean(PC*w))
print("Plain average of Eq.(2) over a period (1/sqrt3):", np.mean(PC), 1/np.sqrt(3))
# D1-only conditional (what Campbell's P[x|R=0] actually describes)
P1,P2,P3,P4 = joint(eta=(1,0,1,1))
pr = (P3+P4)/(P1+P3+P4)
core = abs(x) < 0.5*period*1.01
print("\nIf R=0 were defined as a D1 click only (D2 events discarded): P(R=1|x) range",
      pr[core].min(), pr[core].max(), "(note P(R=0)=1/4 then, not 1/2)")
# Campbell's formula with the correct P(R=0)=1/4 for D1-only: P(R=1|x)= 1/(1+ f), f = P(x|R0)P(R0)/(P(x|R1)P(R1))

print("\n--- Fringe visibility of the pooled erasure subensemble after dividing out the sinc^2 envelope ---")
for lab,kw in [("ideal",{}),("t=0.7",{"t":0.7}),("eta1=.9,eta2=.6",{"eta":(0.9,0.6,1,1)}),("eta1=.9,eta2=.6,t=.7",{"eta":(0.9,0.6,1,1),"t":0.7})]:
    P1,P2,P3,P4 = joint(**kw)
    s=(P1+P2)/np.maximum(env**2,1e-12); s=s[core]
    print(f"{lab:24s} V_pooled = {(s.max()-s.min())/(s.max()+s.min()):.4f}   analytic (eta1-eta2)/(eta1+eta2)*2sqrt(t(1-t)) = ",end="")
    e=kw.get("eta",(1,1,1,1)); t=kw.get("t",.5); print(f"{(e[0]-e[1])/(e[0]+e[1])*2*np.sqrt(t*(1-t)):.4f}")
print("\n--- Unconditioned D0 visibility implied by Campbell's conditionals, vs BSA/BSB reflectance r ---")
for r in [0,0.25,0.5,0.75,1]:
    m = r*1 + (1-r)*(1+np.cos(2*np.pi*x/period))
    print(f"r={r:4.2f}: V_D0 = {(m.max()-m.min())/(m.max()+m.min()):.3f}  (QM: 0 for every r)")
