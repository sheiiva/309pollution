############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################

class Usage():

    def __init__(self):
        self.show()

    def show(self) -> None:

        """
        Show usage of the program.
        """

        print(
            "USAGE\n"
            "\t./309pollution n file x y\n"
            "DESCRIPTION\n"
            "\tn\tnumber of points on the grid axis\n"
            "\tfile\tcsv file containing the data points x;y;p\n"
            "\tx\tabscissa of the point whose pollution level we want to know\n"
            "\ty\tordinate of the point whose pollution level we want to kno"
            )
