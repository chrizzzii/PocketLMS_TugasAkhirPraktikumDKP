class sistemLogin:
    def __init__(self, username, password):
        self.username = username 
        self.password = password
        self.data = {
            "Tito" : {
                "nama"          : "Agustinus Adven Christo",
                "namapanggilan" : "Tito",
                "email" 	    : "Tito@undip.com",
                "password"      : "1234"
        	}
    	}
		
    def cekinputan(self):
    	for value in self.data:
        	if value == self.username:
                    get_data_user = self.data[value]
                    if self.password == get_data_user['password']:
                        return get_data_user
                    else:
                        return False
	
    def ceklogin(self):
        get_data = self.cekinputan()
        if get_data:
            return True
        else:
            return False
    
                      