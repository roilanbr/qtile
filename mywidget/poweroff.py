from libqtile import bar
from libqtile.widget import base
# from libqtile.command import lazy


# class QuickExit(base._TextBox):
class PowerOff(base._TextBox):
    """
    Spanish:
    Un botón para apagar fácilmente la PC modificado del widget QuickExit. Se utilizará el 
    botón "Bottom2" del mouse. Al hacer clic en este botón, una cuenta regresiva comenzará. 
    Si el botón se presiona con en la cuenta regresiva nuevamente, se detendrá el Apagado.

    English:
    A button to easily shutdown the PC  modified  from the QuickExit widget. The button 
    "Bottom1" of the mouse will be used. By clicking this button, a countdown begin to. 
    If the button is pressed with in the countdown again, the Shutdown will stop.
    """

    defaults = [
        ('default_text', '[ Poweroff ]', 'A text displayed as a button'),
        ('countdown_format', '[ {} seconds ]', 'This text is showed when counting down.'),
        ('timer_interval', 1, 'A countdown interval.'),
        ('countdown_start', 5, 'Time to accept the second pushing.'),
    ]

    def __init__(self, widget=bar.CALCULATED, **config):
        base._TextBox.__init__(self, '', widget, **config)
        self.add_defaults(PowerOff.defaults)

        self.is_counting = False
        self.text = self.default_text
        self.countdown = self.countdown_start
        self.__call_later_funcs = []

        self.add_callbacks({'Button1': self.cmd_trigger})

    def __reset(self):
        self.is_counting = False
        self.countdown = self.countdown_start
        self.text = self.default_text
        for f in self.__call_later_funcs:
            f.cancel()

    def update(self):
        if not self.is_counting:
            return

        self.countdown -= 1
        self.text = self.countdown_format.format(self.countdown)
        func = self.timeout_add(self.timer_interval, self.update)
        self.__call_later_funcs.append(func)
        self.draw()

        if self.countdown == 0:
            self.qtile.cmd_spawn("systemctl -i poweroff")
            #self.qtile.cmd_spawn("alacritty -t Apagar")
            return

    def cmd_trigger(self):
        if not self.is_counting:
            self.is_counting = True
            self.update()
        else:
            self.__reset()
            self.draw()