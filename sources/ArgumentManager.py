############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 309pollution         #
#                                          #
############################################


from sources.utils import *


class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        if len(argv) != 5:
            print("ERROR - Wrong number of arguments.")
            return 84
        if not isInt(argv[1]) or not isFloat(argv[3]) or not isFloat(argv[4]):
            print("ERROR - Wrong arguments type.")
            return 84
        if not isFile(argv[2]):
            print(f"ERROR - {argv[2]} no such file.")
            return 84
        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
