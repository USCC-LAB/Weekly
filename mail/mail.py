"""
.. module:: Mail
    :platform: Linux

.. moduleauthor:: Yen-Kuan Wu <yenwu.tw@gmail.com>
"""

class Mail:
    def __init__(self, prot, *argv):
        """
        Args:
            - prot (Instance Object): Protocol instance
            - *argv (Pointer to array): Variable-length argument
        """
        # Declaration
        self.__prot = None

        # Initialization
        self.__prot = prot(*argv)

    def login(self, account, passwd):
        """
        :param account: Mail account
        :param passwd: Mail password
        :type account: string
        :type passwd: string
        :return: Nothing
        :rtype: void
        """
        self.__prot.login(account, passwd)

    def send(self, frm, to, subject, content):
        """
        Args:
            - frm (str): source address of this email
            - to (str): target address of this email
            - subject (str): Subject of this email
            - content (str): Content of this email
        """
        self.__prot.send(frm, to, subject, content)

    def quit(self):
        """
        Close an cleanup
        """
        self.__prot.quit()
