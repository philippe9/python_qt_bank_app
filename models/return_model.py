class ReturnModel :
    login_done = False
    depot_done = False
    retrait_done = False
    transfert_done = False
    message_login = ''
    message_depot = ''
    message_retrait = ''
    message_transfert = ''
    def __init__(self, login_done= False, depot_done= False, retrait_done= False, transfert_done= False, message_login= 'Identifiants incorrects.', message_depot = '',message_retrait = '',message_transfert = ''):
        self.login_done = login_done
        self.depot_done = depot_done
        self.retrait_done = retrait_done
        self.transfert_done = transfert_done
        self.message_login = message_login
        self.message_depot = message_depot
        self.message_retrait = message_retrait
        self.message_transfert = message_transfert