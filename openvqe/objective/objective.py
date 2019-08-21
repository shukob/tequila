from openvqe import OpenVQEModule, OpenVQEParameters
from openvqe.openvqe_abc import parametrized
from openvqe.circuit import QCircuit
from openvqe.hamiltonian import HamiltonianBase
from numpy import asarray


class ObjectiveParameters(OpenVQEParameters):
    # not sure if we will need parameters
    pass


@parametrized(parameter_class=ObjectiveParameters)
class Objective(OpenVQEModule):

    def __post_init__(self, observable=None, unitaries=None):
        if unitaries is None:
            self.unitaries: list = []
        elif hasattr(unitaries, "__iter__") or hasattr(unitaries, "__get_item__"):
            self.unitaries = unitaries
        else:
            self.unitaries = [unitaries]

        self.observable = observable

    def __add__(self, other):
        # todo comming soon
        raise NotImplementedError("+ not implemented yet")

    def __mul__(self, other):
        # todo comming soon
        raise NotImplementedError("* not implemented yet")

    def objective_function(self, values, weights=None):
        """
        The abstract function which defines the operation performed on the expectation values
        The default is summation
        Overwrite this function to get different functions

        Potentially better Idea for the future: Maybe just use objectives as primitives, since they will have +,-,*,...,
        So the functions can be created and differentiated from the outside
        Then overwriting this functions is not necessary anymore

        :param values: Measurement results corresponding to <Psi_i|H|Psi_i> with |Psi_i> = U_i|Psi>
        :param weights: weights on the measurements
        :return:
        """
        if weights is None:
            weights = asarray([1] * len(values))
        values = asarray(values)
        assert (len(weights) == len(values))
        return weights.dot(values)
