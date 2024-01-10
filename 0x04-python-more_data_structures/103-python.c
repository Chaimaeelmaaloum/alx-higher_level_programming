#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
    /**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
}

void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *obj;

    size = ((PyVarObject *)(p))->ob_size;
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        obj = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
