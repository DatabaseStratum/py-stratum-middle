from cleo import Application

from pystratum.command.ConstantsCommand import ConstantsCommand
from pystratum.command.LoaderCommand import LoaderCommand
from pystratum.command.PyStratumCommand import PyStratumCommand
from pystratum.command.WrapperCommand import WrapperCommand


class PyStratumApplication(Application):
    """
    The PyStratum application.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor
        """
        Application.__init__(self, 'pystratum', '0.9.21')

    # ------------------------------------------------------------------------------------------------------------------
    def get_default_commands(self):
        """
        Returns the default commands of this application.

        :rtype: list[cleo.Command]
        """
        commands = Application.get_default_commands(self)

        self.add(ConstantsCommand())
        self.add(LoaderCommand())
        self.add(PyStratumCommand())
        self.add(WrapperCommand())

        return commands

# ----------------------------------------------------------------------------------------------------------------------