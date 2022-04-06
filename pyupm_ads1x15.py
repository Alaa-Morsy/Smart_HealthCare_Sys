# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyupm_ads1x15', [dirname(__file__)])
        except ImportError:
            import _pyupm_ads1x15
            return _pyupm_ads1x15
        if fp is not None:
            try:
                _mod = imp.load_module('_pyupm_ads1x15', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyupm_ads1x15 = swig_import_helper()
    del swig_import_helper
else:
    import _pyupm_ads1x15
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def getVersion():
    return _pyupm_ads1x15.getVersion()
getVersion = _pyupm_ads1x15.getVersion
class IModuleStatus(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IModuleStatus, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IModuleStatus, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def getModuleName(self):
        """
        virtual
        const char* getModuleName()=0

        Returns name of module. This is the string in library name after
        libupm_

        name of module 
        """
        return _pyupm_ads1x15.IModuleStatus_getModuleName(self)


    __swig_destroy__ = _pyupm_ads1x15.delete_IModuleStatus
    __del__ = lambda self: None

IModuleStatus_swigregister = _pyupm_ads1x15.IModuleStatus_swigregister
IModuleStatus_swigregister(IModuleStatus)

class IADC(IModuleStatus):
    """


    Interface for ADC Sensors.

    C++ includes: iADC.hpp 
    """

    __swig_setmethods__ = {}
    for _s in [IModuleStatus]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IADC, name, value)
    __swig_getmethods__ = {}
    for _s in [IModuleStatus]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IADC, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def getResolutionInBits(self):
        """
        virtual
        unsigned int getResolutionInBits()=0 
        """
        return _pyupm_ads1x15.IADC_getResolutionInBits(self)



    def getNumInputs(self):
        """
        virtual unsigned int
        getNumInputs()=0 
        """
        return _pyupm_ads1x15.IADC_getNumInputs(self)



    def getRawValue(self, input):
        """
        virtual uint16_t
        getRawValue(unsigned int input)=0 
        """
        return _pyupm_ads1x15.IADC_getRawValue(self, input)



    def getVoltage(self, input):
        """
        virtual float
        getVoltage(unsigned int input)=0 
        """
        return _pyupm_ads1x15.IADC_getVoltage(self, input)


    __swig_destroy__ = _pyupm_ads1x15.delete_IADC
    __del__ = lambda self: None

IADC_swigregister = _pyupm_ads1x15.IADC_swigregister
IADC_swigregister(IADC)


_pyupm_ads1x15.ADS1X15_ADDRESS_swigconstant(_pyupm_ads1x15)
ADS1X15_ADDRESS = _pyupm_ads1x15.ADS1X15_ADDRESS

_pyupm_ads1x15.ADS1X15_REG_POINTER_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_REG_POINTER_MASK = _pyupm_ads1x15.ADS1X15_REG_POINTER_MASK

_pyupm_ads1x15.ADS1X15_REG_POINTER_CONVERT_swigconstant(_pyupm_ads1x15)
ADS1X15_REG_POINTER_CONVERT = _pyupm_ads1x15.ADS1X15_REG_POINTER_CONVERT

_pyupm_ads1x15.ADS1X15_REG_POINTER_CONFIG_swigconstant(_pyupm_ads1x15)
ADS1X15_REG_POINTER_CONFIG = _pyupm_ads1x15.ADS1X15_REG_POINTER_CONFIG

_pyupm_ads1x15.ADS1X15_REG_POINTER_LOWTHRESH_swigconstant(_pyupm_ads1x15)
ADS1X15_REG_POINTER_LOWTHRESH = _pyupm_ads1x15.ADS1X15_REG_POINTER_LOWTHRESH

_pyupm_ads1x15.ADS1X15_REG_POINTER_HITHRESH_swigconstant(_pyupm_ads1x15)
ADS1X15_REG_POINTER_HITHRESH = _pyupm_ads1x15.ADS1X15_REG_POINTER_HITHRESH

_pyupm_ads1x15.ADS1X15_OS_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_OS_MASK = _pyupm_ads1x15.ADS1X15_OS_MASK

_pyupm_ads1x15.ADS1X15_OS_SINGLE_swigconstant(_pyupm_ads1x15)
ADS1X15_OS_SINGLE = _pyupm_ads1x15.ADS1X15_OS_SINGLE

_pyupm_ads1x15.ADS1X15_OS_BUSY_swigconstant(_pyupm_ads1x15)
ADS1X15_OS_BUSY = _pyupm_ads1x15.ADS1X15_OS_BUSY

_pyupm_ads1x15.ADS1X15_OS_NOTBUSY_swigconstant(_pyupm_ads1x15)
ADS1X15_OS_NOTBUSY = _pyupm_ads1x15.ADS1X15_OS_NOTBUSY

_pyupm_ads1x15.ADS1X15_MUX_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_MASK = _pyupm_ads1x15.ADS1X15_MUX_MASK

_pyupm_ads1x15.ADS1X15_MUX_DIFF_0_1_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_DIFF_0_1 = _pyupm_ads1x15.ADS1X15_MUX_DIFF_0_1

_pyupm_ads1x15.ADS1X15_MUX_DIFF_0_3_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_DIFF_0_3 = _pyupm_ads1x15.ADS1X15_MUX_DIFF_0_3

_pyupm_ads1x15.ADS1X15_MUX_DIFF_1_3_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_DIFF_1_3 = _pyupm_ads1x15.ADS1X15_MUX_DIFF_1_3

_pyupm_ads1x15.ADS1X15_MUX_DIFF_2_3_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_DIFF_2_3 = _pyupm_ads1x15.ADS1X15_MUX_DIFF_2_3

_pyupm_ads1x15.ADS1X15_MUX_SINGLE_0_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_SINGLE_0 = _pyupm_ads1x15.ADS1X15_MUX_SINGLE_0

_pyupm_ads1x15.ADS1X15_MUX_SINGLE_1_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_SINGLE_1 = _pyupm_ads1x15.ADS1X15_MUX_SINGLE_1

_pyupm_ads1x15.ADS1X15_MUX_SINGLE_2_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_SINGLE_2 = _pyupm_ads1x15.ADS1X15_MUX_SINGLE_2

_pyupm_ads1x15.ADS1X15_MUX_SINGLE_3_swigconstant(_pyupm_ads1x15)
ADS1X15_MUX_SINGLE_3 = _pyupm_ads1x15.ADS1X15_MUX_SINGLE_3

_pyupm_ads1x15.ADS1X15_PGA_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_PGA_MASK = _pyupm_ads1x15.ADS1X15_PGA_MASK

_pyupm_ads1x15.ADS1X15_PGA_6_144V_swigconstant(_pyupm_ads1x15)
ADS1X15_PGA_6_144V = _pyupm_ads1x15.ADS1X15_PGA_6_144V

_pyupm_ads1x15.ADS1X15_PGA_4_096V_swigconstant(_pyupm_ads1x15)
ADS1X15_PGA_4_096V = _pyupm_ads1x15.ADS1X15_PGA_4_096V

_pyupm_ads1x15.ADS1X15_PGA_2_048V_swigconstant(_pyupm_ads1x15)
ADS1X15_PGA_2_048V = _pyupm_ads1x15.ADS1X15_PGA_2_048V

_pyupm_ads1x15.ADS1X15_PGA_1_024V_swigconstant(_pyupm_ads1x15)
ADS1X15_PGA_1_024V = _pyupm_ads1x15.ADS1X15_PGA_1_024V

_pyupm_ads1x15.ADS1X15_PGA_0_512V_swigconstant(_pyupm_ads1x15)
ADS1X15_PGA_0_512V = _pyupm_ads1x15.ADS1X15_PGA_0_512V

_pyupm_ads1x15.ADS1X15_PGA_0_256V_swigconstant(_pyupm_ads1x15)
ADS1X15_PGA_0_256V = _pyupm_ads1x15.ADS1X15_PGA_0_256V

_pyupm_ads1x15.ADS1X15_MODE_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_MODE_MASK = _pyupm_ads1x15.ADS1X15_MODE_MASK

_pyupm_ads1x15.ADS1X15_MODE_CONTIN_swigconstant(_pyupm_ads1x15)
ADS1X15_MODE_CONTIN = _pyupm_ads1x15.ADS1X15_MODE_CONTIN

_pyupm_ads1x15.ADS1X15_MODE_SINGLE_swigconstant(_pyupm_ads1x15)
ADS1X15_MODE_SINGLE = _pyupm_ads1x15.ADS1X15_MODE_SINGLE

_pyupm_ads1x15.ADS1X15_DR_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_DR_MASK = _pyupm_ads1x15.ADS1X15_DR_MASK

_pyupm_ads1x15.ADS1X15_CMODE_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_CMODE_MASK = _pyupm_ads1x15.ADS1X15_CMODE_MASK

_pyupm_ads1x15.ADS1X15_CMODE_TRAD_swigconstant(_pyupm_ads1x15)
ADS1X15_CMODE_TRAD = _pyupm_ads1x15.ADS1X15_CMODE_TRAD

_pyupm_ads1x15.ADS1X15_CMODE_WINDOW_swigconstant(_pyupm_ads1x15)
ADS1X15_CMODE_WINDOW = _pyupm_ads1x15.ADS1X15_CMODE_WINDOW

_pyupm_ads1x15.ADS1X15_CPOL_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_CPOL_MASK = _pyupm_ads1x15.ADS1X15_CPOL_MASK

_pyupm_ads1x15.ADS1X15_CPOL_ACTVLOW_swigconstant(_pyupm_ads1x15)
ADS1X15_CPOL_ACTVLOW = _pyupm_ads1x15.ADS1X15_CPOL_ACTVLOW

_pyupm_ads1x15.ADS1X15_CPOL_ACTVHI_swigconstant(_pyupm_ads1x15)
ADS1X15_CPOL_ACTVHI = _pyupm_ads1x15.ADS1X15_CPOL_ACTVHI

_pyupm_ads1x15.ADS1X15_CLAT_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_CLAT_MASK = _pyupm_ads1x15.ADS1X15_CLAT_MASK

_pyupm_ads1x15.ADS1X15_CLAT_NONLAT_swigconstant(_pyupm_ads1x15)
ADS1X15_CLAT_NONLAT = _pyupm_ads1x15.ADS1X15_CLAT_NONLAT

_pyupm_ads1x15.ADS1X15_CLAT_LATCH_swigconstant(_pyupm_ads1x15)
ADS1X15_CLAT_LATCH = _pyupm_ads1x15.ADS1X15_CLAT_LATCH

_pyupm_ads1x15.ADS1X15_CQUE_MASK_swigconstant(_pyupm_ads1x15)
ADS1X15_CQUE_MASK = _pyupm_ads1x15.ADS1X15_CQUE_MASK
class ADS1X15(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ADS1X15, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ADS1X15, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GAIN_TWOTHIRDS = _pyupm_ads1x15.ADS1X15_GAIN_TWOTHIRDS
    GAIN_ONE = _pyupm_ads1x15.ADS1X15_GAIN_ONE
    GAIN_TWO = _pyupm_ads1x15.ADS1X15_GAIN_TWO
    GAIN_FOUR = _pyupm_ads1x15.ADS1X15_GAIN_FOUR
    GAIN_EIGHT = _pyupm_ads1x15.ADS1X15_GAIN_EIGHT
    GAIN_SIXTEEN = _pyupm_ads1x15.ADS1X15_GAIN_SIXTEEN
    DIFF_0_1 = _pyupm_ads1x15.ADS1X15_DIFF_0_1
    DIFF_0_3 = _pyupm_ads1x15.ADS1X15_DIFF_0_3
    DIFF_1_3 = _pyupm_ads1x15.ADS1X15_DIFF_1_3
    DIFF_2_3 = _pyupm_ads1x15.ADS1X15_DIFF_2_3
    SINGLE_0 = _pyupm_ads1x15.ADS1X15_SINGLE_0
    SINGLE_1 = _pyupm_ads1x15.ADS1X15_SINGLE_1
    SINGLE_2 = _pyupm_ads1x15.ADS1X15_SINGLE_2
    SINGLE_3 = _pyupm_ads1x15.ADS1X15_SINGLE_3
    CQUE_1CONV = _pyupm_ads1x15.ADS1X15_CQUE_1CONV
    CQUE_2CONV = _pyupm_ads1x15.ADS1X15_CQUE_2CONV
    CQUE_4CONV = _pyupm_ads1x15.ADS1X15_CQUE_4CONV
    CQUE_NONE = _pyupm_ads1x15.ADS1X15_CQUE_NONE
    THRESH_LOW = _pyupm_ads1x15.ADS1X15_THRESH_LOW
    THRESH_HIGH = _pyupm_ads1x15.ADS1X15_THRESH_HIGH
    CONVERSION_RDY = _pyupm_ads1x15.ADS1X15_CONVERSION_RDY
    THRESH_DEFAULT = _pyupm_ads1x15.ADS1X15_THRESH_DEFAULT
    SPS_DEFAULT = _pyupm_ads1x15.ADS1X15_SPS_DEFAULT
    __swig_destroy__ = _pyupm_ads1x15.delete_ADS1X15
    __del__ = lambda self: None

    def name(self):
        """
        std::string name()

        Returns the name of the sensor 
        """
        return _pyupm_ads1x15.ADS1X15_name(self)



    def getLastSample(self, *args):
        """
        float
        getLastSample(int reg=ADS1X15_REG_POINTER_CONVERT)

        Returns the contents of conversion register without performing a
        conversion operation. Will use a multiplier based on the current gain
        setting to give the voltage as a float. Used internally to return the
        HI and LOW threshold values.

        Parameters:
        -----------

        reg:  uint8_t value specifying register to read. Should generally be
        called with no parameter. 
        """
        return _pyupm_ads1x15.ADS1X15_getLastSample(self, *args)



    def getSample(self, *args):
        """
        float
        getSample(ADSMUXMODE mode=ADS1X15::DIFF_0_1)

        Performs a read as specified by ADS1X15::ADSMUXMOE and returns the
        value as a float. Uses getLastSample() internally to return voltage
        value.

        mode ADSMUXMODE specifying inputs to be sampled. 
        """
        return _pyupm_ads1x15.ADS1X15_getSample(self, *args)



    def getGain(self):
        """
        ADSGAIN getGain()

        Returns the current gain setting being used by the device as an
        ADSGAIN value. 
        """
        return _pyupm_ads1x15.ADS1X15_getGain(self)



    def setGain(self, *args):
        """
        void setGain(ADSGAIN
        gain=ADS1X15::GAIN_TWO)

        Sets the PGA gain bits to the desired gain. Default is +/- 2.094
        volts.

        Parameters:
        -----------

        gain:  ADSGAIN value reprenting the desired gain. See warnings in spec
        sheet. 
        """
        return _pyupm_ads1x15.ADS1X15_setGain(self, *args)



    def getSPS(self):
        """
        ADSSAMPLERATE
        getSPS(void)

        Returns the current device sample rate a an ADSSAMPLERATE value. 
        """
        return _pyupm_ads1x15.ADS1X15_getSPS(self)



    def setSPS(self, rate):
        """
        void
        setSPS(ADSSAMPLERATE rate)

        Sets the sample rate of the device. This function needs to be overrode
        in subclasses as the ADS1115 and ADS1015 have different data rates.

        Parameters:
        -----------

        ADSSAMPLERATE:  enum SPS_DEFAULT = 0x0080 
        """
        return _pyupm_ads1x15.ADS1X15_setSPS(self, rate)



    def getCompMode(self):
        """
        bool
        getCompMode(void)

        Returns the comparator mode. False = Traditional comparator with
        Hysteresis (default) True = Window Comparator 
        """
        return _pyupm_ads1x15.ADS1X15_getCompMode(self)



    def setCompMode(self, mode=False):
        """
        void
        setCompMode(bool mode=false)

        Sets the comparator mode of the device.

        Parameters:
        -----------

        mode:  bool value denoting mode. False = Traditional comparator with
        Hysteresis (default) True = Window Comparator 
        """
        return _pyupm_ads1x15.ADS1X15_setCompMode(self, mode)



    def getCompPol(self):
        """
        bool
        getCompPol(void)

        Get comparator polarity. Reports the polarity of the ALERT/RDY pin.
        Returns: False = Active Low (default) True = Active High 
        """
        return _pyupm_ads1x15.ADS1X15_getCompPol(self)



    def setCompPol(self, mode=False):
        """
        void setCompPol(bool
        mode=false)

        Sets the comparator polarity. Controls the polarity of the ALERT/RDY
        pin.

        Parameters:
        -----------

        mode:  bool. False = Active Low (default) True = Active High 
        """
        return _pyupm_ads1x15.ADS1X15_setCompPol(self, mode)



    def getCompLatch(self):
        """
        bool
        getCompLatch(void)

        Returns bool representing the state of the comparator latching
        functionality. False = Non Latching comparator (default) True =
        Latching Comparator 
        """
        return _pyupm_ads1x15.ADS1X15_getCompLatch(self)



    def setCompLatch(self, mode=False):
        """
        void
        setCompLatch(bool mode=false)

        Sets bit controlling comparator operation.

        Parameters:
        -----------

        mode:  bool False = Non Latching comparator (default) True = Latching
        Comparator 
        """
        return _pyupm_ads1x15.ADS1X15_setCompLatch(self, mode)



    def getCompQue(self):
        """
        ADSCOMP
        getCompQue(void)

        Returns ADSCOMP value representing the state of comparator queue.

        CQUE_1CONV = Assert after one conversion CQUE_2CONV = Assert after two
        conversions CQUE_2CONV = Assert after four conversions CQUE_NONE =
        Disable comparator (default) 
        """
        return _pyupm_ads1x15.ADS1X15_getCompQue(self)



    def setCompQue(self, *args):
        """
        void
        setCompQue(ADSCOMP mode=ADS1X15::CQUE_NONE)

        Sets bits controlling Comparator queue operation.

        Parameters:
        -----------

        mode:  ADSCOMP enum. CQUE_1CONV = Assert after one conversion
        CQUE_2CONV = Assert after two conversions CQUE_2CONV = Assert after
        four conversions CQUE_NONE = Disable comparator (default) 
        """
        return _pyupm_ads1x15.ADS1X15_setCompQue(self, *args)



    def getContinuous(self):
        """
        bool
        getContinuous(void)

        Returns bool reflecting state of device mode bit.

        False = Power Down Single shot mode (default) True = Continuous
        conversion mode 
        """
        return _pyupm_ads1x15.ADS1X15_getContinuous(self)



    def setContinuous(self, mode=False):
        """
        void
        setContinuous(bool mode=false)

        Sets the state of device mode but.

        Parameters:
        -----------

        mode:  bool False = Power Down Single shot mode (default) True =
        Continuous conversion mode 
        """
        return _pyupm_ads1x15.ADS1X15_setContinuous(self, mode)



    def getThresh(self, *args):
        """
        float
        getThresh(ADSTHRESH reg=THRESH_DEFAULT)

        Returns current high or low threshold setting.

        Parameters:
        -----------

        reg:  ADSTHRES enum value. Returns 0.0 unless THRESH_HIGH or
        THRESH_LOW requested. 
        """
        return _pyupm_ads1x15.ADS1X15_getThresh(self, *args)



    def setThresh(self, *args):
        """
        void
        setThresh(ADSTHRESH reg=THRESH_DEFAULT, float value=0.0)

        Sets threshold levels or configures for conversion ready operation of
        ALERT/RDY output.

        Parameters:
        -----------

        reg:  ADSTHRESH enum

        value:  float value to set threshold register to.

        THRESH_LOW = Sets low thresh register. THRESH_HIGH = Sets high thresh
        register. CONVERSION_RDY = Configures conversion ready operation
        THRESH_DEFAULT = resets high/low registers to startup values. 
        """
        return _pyupm_ads1x15.ADS1X15_setThresh(self, *args)


ADS1X15_swigregister = _pyupm_ads1x15.ADS1X15_swigregister
ADS1X15_swigregister(ADS1X15)


_pyupm_ads1x15.ADS1115_CONVERSIONDELAY_swigconstant(_pyupm_ads1x15)
ADS1115_CONVERSIONDELAY = _pyupm_ads1x15.ADS1115_CONVERSIONDELAY

_pyupm_ads1x15.ADS1115_DR_MASK_swigconstant(_pyupm_ads1x15)
ADS1115_DR_MASK = _pyupm_ads1x15.ADS1115_DR_MASK

_pyupm_ads1x15.ADS1115_DR_8SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_8SPS = _pyupm_ads1x15.ADS1115_DR_8SPS

_pyupm_ads1x15.ADS1115_DR_16SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_16SPS = _pyupm_ads1x15.ADS1115_DR_16SPS

_pyupm_ads1x15.ADS1115_DR_32SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_32SPS = _pyupm_ads1x15.ADS1115_DR_32SPS

_pyupm_ads1x15.ADS1115_DR_64SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_64SPS = _pyupm_ads1x15.ADS1115_DR_64SPS

_pyupm_ads1x15.ADS1115_DR_128SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_128SPS = _pyupm_ads1x15.ADS1115_DR_128SPS

_pyupm_ads1x15.ADS1115_DR_250SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_250SPS = _pyupm_ads1x15.ADS1115_DR_250SPS

_pyupm_ads1x15.ADS1115_DR_475SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_475SPS = _pyupm_ads1x15.ADS1115_DR_475SPS

_pyupm_ads1x15.ADS1115_DR_860SPS_swigconstant(_pyupm_ads1x15)
ADS1115_DR_860SPS = _pyupm_ads1x15.ADS1115_DR_860SPS
class ADS1115(ADS1X15):
    """


    API for ADS1115.

    ID: ADS1115

    Name: 16-bit ADC with Integrated MUX, PGA, Comparator, Oscillator, and
    Reference

    Category: electric

    Manufacturer: ti adafruit

    Connection: i2c

    Link:http://www.ti.com/lit/ds/symlink/ads1115.pdf  The ADS1113,
    ADS1114, and ADS1115 are precision analog-to-digital converters (ADCs)
    with 16 bits of resolution offered in an ultra-small, leadless QFN-10
    package or an MSOP-10 package. The ADS1113/4/5 are designed with
    precision, power, and ease of implementation in mind. The ADS1113/4/5
    feature an onboard reference and oscillator. Data is transferred via
    an I2C-compatible serial interface; four I2C slave addresses can be
    selected. The ADS1113/4/5 operate from a single power supply ranging
    from 2.0V to 5.5V. The ADS1113/4/5 can perform conversions at rates up
    to 860 samples per second (SPS). An onboard PGA is available on the
    ADS1114 and ADS1115 that offers input ranges from the supply to as low
    as +/- 256mV, allowing both large and small signals to be measured
    with high resolution. The ADS1115 also features an input multiplexer
    (MUX) that provides two differential or four single-ended inputs. The
    ADS1113/4/5 operate either in continuous conversion mode or a single-
    shot mode that automatically powers down after a conversion and
    greatly reduces current consumption during idle periods. The
    ADS1113/4/5 are specified from -40 deg C to +125 deg C.

    Tested with DIYMall ADS1115 board. Also available from
    Adafruit:https://www.adafruit.com/products/1085

    C++ includes: ads1115.hpp 
    """

    __swig_setmethods__ = {}
    for _s in [ADS1X15]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ADS1115, name, value)
    __swig_getmethods__ = {}
    for _s in [ADS1X15]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ADS1115, name)
    __repr__ = _swig_repr
    SPS_8 = _pyupm_ads1x15.ADS1115_SPS_8
    SPS_16 = _pyupm_ads1x15.ADS1115_SPS_16
    SPS_32 = _pyupm_ads1x15.ADS1115_SPS_32
    SPS_64 = _pyupm_ads1x15.ADS1115_SPS_64
    SPS_128 = _pyupm_ads1x15.ADS1115_SPS_128
    SPS_250 = _pyupm_ads1x15.ADS1115_SPS_250
    SPS_475 = _pyupm_ads1x15.ADS1115_SPS_475
    SPS_860 = _pyupm_ads1x15.ADS1115_SPS_860

    def __init__(self, bus, address=0x48):
        """
        ADS1115(int bus,
        uint8_t address=0x48)

        ADS1X15 constructor

        Parameters:
        -----------

        bus:  i2c bus the sensor is attached to.

        address:  Device address. Default is 0x48. 
        """
        this = _pyupm_ads1x15.new_ADS1115(bus, address)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pyupm_ads1x15.delete_ADS1115
    __del__ = lambda self: None

    def setSPS(self, *args):
        """
        void setSPS(ADSDATARATE
        rate=ADS1115::SPS_128)

        Sets the sample rate of the device. This function needs to be
        overridden in subclasses as the ADS1115 and ADS1015 have different
        sample rates.

        Parameters:
        -----------

        rate:  ADSSAMPLERATE enum 
        """
        return _pyupm_ads1x15.ADS1115_setSPS(self, *args)


ADS1115_swigregister = _pyupm_ads1x15.ADS1115_swigregister
ADS1115_swigregister(ADS1115)


_pyupm_ads1x15.ADS1015_VREF_swigconstant(_pyupm_ads1x15)
ADS1015_VREF = _pyupm_ads1x15.ADS1015_VREF

_pyupm_ads1x15.ADS1015_CONVERSIONDELAY_swigconstant(_pyupm_ads1x15)
ADS1015_CONVERSIONDELAY = _pyupm_ads1x15.ADS1015_CONVERSIONDELAY

_pyupm_ads1x15.ADS1015_DR_MASK_swigconstant(_pyupm_ads1x15)
ADS1015_DR_MASK = _pyupm_ads1x15.ADS1015_DR_MASK

_pyupm_ads1x15.ADS1015_DR_128SPS_swigconstant(_pyupm_ads1x15)
ADS1015_DR_128SPS = _pyupm_ads1x15.ADS1015_DR_128SPS

_pyupm_ads1x15.ADS1015_DR_250SPS_swigconstant(_pyupm_ads1x15)
ADS1015_DR_250SPS = _pyupm_ads1x15.ADS1015_DR_250SPS

_pyupm_ads1x15.ADS1015_DR_490SPS_swigconstant(_pyupm_ads1x15)
ADS1015_DR_490SPS = _pyupm_ads1x15.ADS1015_DR_490SPS

_pyupm_ads1x15.ADS1015_DR_920SPS_swigconstant(_pyupm_ads1x15)
ADS1015_DR_920SPS = _pyupm_ads1x15.ADS1015_DR_920SPS

_pyupm_ads1x15.ADS1015_DR_1600SPS_swigconstant(_pyupm_ads1x15)
ADS1015_DR_1600SPS = _pyupm_ads1x15.ADS1015_DR_1600SPS

_pyupm_ads1x15.ADS1015_DR_2400SPS_swigconstant(_pyupm_ads1x15)
ADS1015_DR_2400SPS = _pyupm_ads1x15.ADS1015_DR_2400SPS

_pyupm_ads1x15.ADS1015_DR_3300SPS_swigconstant(_pyupm_ads1x15)
ADS1015_DR_3300SPS = _pyupm_ads1x15.ADS1015_DR_3300SPS
class ADS1015(ADS1X15, IADC):
    """


    API for ADS1015.

    ID: ADS1015

    Name: 12-bit ADC with Integrated MUX, PGA, Comparator, Oscillator, and
    Reference

    Category: electric

    Manufacturer: ti adafruit

    Connection: i2c

    Link:http://www.ti.com/lit/ds/symlink/ads1015.pdf  The ADS1013,
    ADS1014, and ADS1015 are precision analog-to-digital converters (ADCs)
    with 12 bits of resolution offered in an ultra-small, leadless QFN-10
    package or an MSOP-10 package. The ADS1013/4/5 are designed with
    precision, power, and ease of implementation in mind. The ADS1013/4/5
    feature an onboard reference and oscillator. Data is transferred via
    an I2C-compatible serial interface; four I2C slave addresses can be
    selected. The ADS1013/4/5 operate from a single power supply ranging
    from 2.0V to 5.5V. The ADS1013/4/5 can perform conversions at rates up
    to 3300 samples per second (SPS). An onboard PGA is available on the
    ADS1014 and ADS1015 that offers input ranges from the supply to as low
    as +/- 256mV, allowing both large and small signals to be measured
    with high resolution. The ADS1015 also features an input multiplexer
    (MUX) that provides two differential or four single-ended inputs. The
    ADS1013/4/5 operate either in continuous conversion mode or a single-
    shot mode that automatically powers down after a conversion and
    greatly reduces current consumption during idle periods. The
    ADS1013/4/5 are specified from -40 deg C to +125 deg C.

    Tested with Adafriut ADS1015
    board:https://www.adafruit.com/products/1083

    C++ includes: ads1015.hpp 
    """

    __swig_setmethods__ = {}
    for _s in [ADS1X15, IADC]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ADS1015, name, value)
    __swig_getmethods__ = {}
    for _s in [ADS1X15, IADC]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ADS1015, name)
    __repr__ = _swig_repr
    SPS_128 = _pyupm_ads1x15.ADS1015_SPS_128
    SPS_250 = _pyupm_ads1x15.ADS1015_SPS_250
    SPS_490 = _pyupm_ads1x15.ADS1015_SPS_490
    SPS_920 = _pyupm_ads1x15.ADS1015_SPS_920
    SPS_1600 = _pyupm_ads1x15.ADS1015_SPS_1600
    SPS_2400 = _pyupm_ads1x15.ADS1015_SPS_2400
    SPS_3300 = _pyupm_ads1x15.ADS1015_SPS_3300

    def __init__(self, bus, address=0x48, vref=2.048):
        """
        ADS1015(int bus,
        uint8_t address=0x48, float vref=ADS1015_VREF)

        ADS1015 constructor

        This constructor includes a vref parameter that can be used to set
        gain so it matches full scale value of input

        Parameters:
        -----------

        bus:  i2c bus the sensor is attached to.

        address:  Optional device address. Default is 0x48.

        vref:  Optional reference (i.e. half full swing) voltage. Default is
        2.048V 
        """
        this = _pyupm_ads1x15.new_ADS1015(bus, address, vref)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pyupm_ads1x15.delete_ADS1015
    __del__ = lambda self: None

    def setSPS(self, *args):
        """
        void
        setSPS(ADSSAMPLERATE rate=SPS_1600)

        Sets the sample rate of the device. This function needs to be
        overridden in subclasses as the ADS1115 and ADS1015 have different
        sample rates.

        Parameters:
        -----------

        rate:  ADSSAMPLERATE enum 
        """
        return _pyupm_ads1x15.ADS1015_setSPS(self, *args)



    def getNumInputs(self):
        """
        unsigned int
        getNumInputs()

        Get number of inputs

        number of inputs 
        """
        return _pyupm_ads1x15.ADS1015_getNumInputs(self)



    def getRawValue(self, input):
        """
        uint16_t
        getRawValue(unsigned int input)

        Read current value for current single ended analogue input

        current conversion value 
        """
        return _pyupm_ads1x15.ADS1015_getRawValue(self, input)



    def getVoltage(self, input):
        """
        float
        getVoltage(unsigned int input)

        Read current voltage for current single ended analogue input

        current voltage 
        """
        return _pyupm_ads1x15.ADS1015_getVoltage(self, input)



    def getResolutionInBits(self):
        """
        unsigned
        int getResolutionInBits()

        Read current voltage for current single ended analogue input

        current voltage 
        """
        return _pyupm_ads1x15.ADS1015_getResolutionInBits(self)



    def getModuleName(self):
        """
        const char *
        getModuleName()

        Returns module name

        modulename as const char* 
        """
        return _pyupm_ads1x15.ADS1015_getModuleName(self)


ADS1015_swigregister = _pyupm_ads1x15.ADS1015_swigregister
ADS1015_swigregister(ADS1015)

# This file is compatible with both classic and new-style classes.
