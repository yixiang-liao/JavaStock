package stockapp;

import org.python.core.PyInteger;
import org.python.core.PyFunction;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;

public class StockPyClass {
    public static void StockPy(String ID){
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.execfile("C:\\Users\\User\\Documents\\NetBeansProjects\\StockApp\\src\\stock_py\\stock.py");
        PyFunction pyFunction = interpreter.get("implement", PyFunction.class);
        PyObject pyobj = pyFunction.__call__(new PyInteger(ID)); 
    }
}
