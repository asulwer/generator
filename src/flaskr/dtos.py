class TemplateData:
    def __init__(self,gp=False,sp=False,sap=False,ss=False,saco=False,sacf=False):
        self._glowPlugs = gp
        self._switchPump = sp
        self._switchAuxPump = sap
        self._switchStarter = ss
        self._switchACOnInterupt = saco
        self._switchACOffInterupt = sacf

        @property
        def glowPlugs(self):
            return self._glowPlugs

        @property
        def switchPump(self):
            return self._switchPump

        @property
        def switchAuxPump(self):
            return self._switchAuxPump
        
        @property
        def switchStarter(self):
            return self._switchStarter
        
        @property
        def switchACOnInterupt(self):
            return self._switchACOnInterupt
        
        @property
        def switchACOffInterupt(self):
            return self._switchACOffInterupt
        
        @glowPlugs.setter
        def glowPlugs(self, value):
            if isinstance(value, bool):
                self._glowPlugs = value
            else:
                raise ValueError("glowPlugs must be boolean")

        @switchPump.setter
        def switchPump(self, value):
            if isinstance(value, bool):
                self._switchPump = value
            else:
                raise ValueError("glowPlugs must be boolean")

        @switchAuxPump.setter
        def switchAuxPump(self, value):
            if isinstance(value, bool):
                self._switchAuxPump = value
            else:
                raise ValueError("glowPlugs must be boolean")

        @switchStarter.setter
        def switchStarter(self, value):
            if isinstance(value, bool):
                self._switchStarter = value
            else:
                raise ValueError("glowPlugs must be boolean")

        @switchACOnInterupt.setter
        def switchACOnInterupt(self, value):
            if isinstance(value, bool):
                self._switchACOnInterupt = value
            else:
                raise ValueError("glowPlugs must be boolean")

        @switchACOffInterupt.setter
        def switchACOffInterupt(self, value):
            if isinstance(value, bool):
                self._switchACOffInterupt = value
            else:
                raise ValueError("glowPlugs must be boolean")