# -*- coding: utf-8 -*-

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.Electrical.coordinate_transformation import n2dq
from numpy import (
    zeros,
    linspace,
    pi,
    split,
)

# import matplotlib.pyplot as plt


def comp_fluxlinkage(self, output):
    """Compute using FEMM the flux linkage

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    """

    qs = output.simu.machine.stator.winding.qs
    p = output.simu.machine.stator.winding.p
    Nt_tot = self.Nt_tot

    # Store data to be replaced
    angle_rotor = output.elec.angle_rotor
    Is = output.elec.Is
    Ir = output.elec.Ir

    # Set currents at 0A for the FEMM simulation
    output.elec.Is = zeros((Nt_tot, qs))
    output.elec.Ir = zeros((Nt_tot, qs))

    # Set the symmetry factor if needed
    if self.is_symmetry_a:
        sym = self.sym_a
        if self.is_antiper_a:
            sym *= 2
        if self.is_sliding_band:
            self.is_sliding_band = (
                True  # When there is a symmetry, there must be a sliding band.
            )
    else:
        sym = 1

    # Compute initial angle from unit mmf
    alpha_0 = 1.31 - pi / 2 / p  # TODO replace by comp_angle_d_axis

    # Compute rotation direction from unit mmf
    rot_dir = 1  # TODO replace by comp_rot_dir

    # Set rotor angle for the FEMM simulation
    angle = linspace(0, 2 * pi / sym, Nt_tot)
    output.elec.angle_rotor = angle

    # Define angle for the flux linkage postprocessing
    mmf_angle = rot_dir * (angle - alpha_0)

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    FEMM_dict = draw_FEMM(
        output,
        is_mmfr=self.is_mmfr,
        is_mmfs=self.is_mmfs,
        sym=sym,
        is_antiper=self.is_antiper_a,
        type_calc_leakage=self.type_calc_leakage,
    )

    # Solve for all time step and store all the results in output
    Phi_wind = self.solve_FEMM(output, sym, FEMM_dict)
    Flux_link = min(n2dq(Phi_wind, p * mmf_angle, n=qs)[0])
    output.elec.EEC_dict["Phi_wind"] = Flux_link

    # time = linspace(0, Nt_tot, Nt_tot)
    # flux = split(Phi_wind, 3, axis=1)
    # fluxdq = split(n2dq(Phi_wind, p * mmf_angle, n=qs), 2, axis=1)
    # fig = plt.figure()
    # plt.plot(time, flux[0], color="tab:blue", label="A")
    # plt.plot(time, flux[1], color="tab:red", label="B")
    # plt.plot(time, flux[2], color="tab:olive", label="C")
    # plt.plot(time, fluxdq[0], color="k", label="D")
    # plt.plot(time, fluxdq[1], color="g", label="Q")
    # plt.legend()
    # fig.savefig("C:\\Users\\HP\\Documents\\Helene\\test_fluxlinkage_dq.png")

    # Reinitialize replaced data
    output.elec.angle_rotor = angle_rotor
    output.elec.Is = Is
    output.elec.Ir = Ir
