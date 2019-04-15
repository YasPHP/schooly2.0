from greeting import Greeting

class Welcome(Greeting):

    def __init__(self, greeting, username = None):
        """
        Constructor to build a welcome object.

        Parameters
        ----------
        greeting : str
            The greeting presented to the user's home dashboard

        username: str
            The username presented to the home dashboard

        Returns
        -------
        None
        """

        super().__init__(greeting)
        self.username = username

    def __str__(self):
        """
        Returns
        -------
        string
        """
        return super().__str__() 

    def display(self) -> str:
        """
        This function displays the username alongside a greeting message.

        Parameters
        ----------
        none

        Returns
        -------
        string
        """

        user = self.username 

        if user is not None:
            return "Welcome {}!\n".format(user) + super().__str__()
        else:
            return super().__str__()