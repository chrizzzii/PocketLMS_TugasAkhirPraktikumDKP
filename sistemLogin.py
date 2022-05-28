class sistemLogin:
    def __init__(self, email, password):
        self.email = email 
        self.password = password
        self.data = {
            "tito@gmail.com" : {
                "nama"          : "Agustinus Adven Christo",
                "namapanggilan" : "Tito",
                "email" 	    : "Tito@undip.com",
                "password"      : "1234"
        	}
    	}
		
    def cekinputan(self):
    	for value in self.data:
        	if value == self.email:
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
    
                      