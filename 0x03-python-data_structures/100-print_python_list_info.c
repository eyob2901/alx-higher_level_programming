#include <Python.h>
void print_python_list_info(PyObject *p)
{
printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (Py_ssize_t i = 0; i < Py_SIZE(p); i++)
printf("Element %ld: %s\n", i, ((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
}
