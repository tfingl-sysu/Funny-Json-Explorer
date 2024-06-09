# icon_family的实现,目前仅试下两种
class Icon:
    def setIcon(self,icon):
        if icon=='poker':
            return pokerIcon()
        elif icon=='music':
            return musicIcon()
        else:
            return self
    def print_node(self):
        print(' ',end='')
    def print_leaf(self):
        print(' ',end='')
class pokerIcon(Icon):
    def print_node(self):
        print('\u2661',end='')
    def print_leaf(self):
        print('\u2662',end='') 
class musicIcon(Icon):
    def print_node(self):
        print('\u2669',end='')
    def print_leaf(self):
=======
# icon_family的实现,目前仅试下两种
class Icon:
    def setIcon(self,icon):
        if icon=='poker':
            return pokerIcon()
        elif icon=='music':
            return musicIcon()
        else:
            return self
    def print_node(self):
        print(' ',end='')
    def print_leaf(self):
        print(' ',end='')
class pokerIcon(Icon):
    def print_node(self):
        print('\u2661',end='')
    def print_leaf(self):
        print('\u2662',end='') 
class musicIcon(Icon):
    def print_node(self):
        print('\u2669',end='')
    def print_leaf(self):
>>>>>>> 53139399b378f878de60ae95f2179f5fad019f86
        print('\u266a',end='')
