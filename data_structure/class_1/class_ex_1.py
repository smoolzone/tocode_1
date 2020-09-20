class LightBulb:
    def __init__(self):
        self.is_lights_on = False
        self.is_lights_off = True

    def lights_on(self):
        if not self.is_lights_on:
            print('on')
            self.is_lights_on = True

    def lights_off(self):
        if self.is_lights_off:
            print('off')
            self.is_lights_on = False


l1 = LightBulb()
l2 = LightBulb()
l56 = LightBulb()

l1.lights_on()
l56.lights_off()

print(l1.is_lights_on)
print(l2.is_lights_on)
print(l56.is_lights_off)
