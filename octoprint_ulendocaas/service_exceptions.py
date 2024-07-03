class ChirpResultError(Exception): pass
class NoSignalError(ChirpResultError): pass
class SignalSyncError(ChirpResultError): pass

class SolverError(Exception): pass
class NoQualifiedSolution(SolverError): pass
class NoVibrationDetected(SolverError): pass

class AutocalInternalServerError(Exception): pass
