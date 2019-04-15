from datetime import datetime

class Greeting: 
    """
    A Greeting object that holds the information that will be presented to the user upon web app opening. 

    Presents attributes of greeting object based on inputted username and randomly generated greeting message with a fun website.
    The content of attribute will be dependent on an implemented random generator. 

    Attributes
    ----------
     greeting: str
           The greeting presented to the user's home dashboard
    """
    def __init__(self, greeting): 
        """
        Constructor to build a greeting object.

        Parameters
        ----------
        greeting : str
            The greeting presented to the user's home dashboard

        Returns
        -------
        None
        """
        self.greeting = greeting

    def __str__(self):
        """
        Returns
        -------
        string
        """
        return self.greeting

    def display(self, *args, **kwargs):
        """
        Returns
        -------
        string
        """
        return "{}\n{}".format(self.__str__(), datetime.now())


