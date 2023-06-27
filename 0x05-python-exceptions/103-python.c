#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{

Py_ssize_t size, i;
PyObject *item;
const char *type;

if (!PyList_Check(p))

printf("[ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
type = Py_TYPE(item)->tp_name;

printf("Element %ld: %s\n", i, type);

if (strcmp(type, "bytes") == 0)
print_python_bytes(item);
else if (strcmp(type, "float") == 0)
print_python_float(item);
}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *data;

if (!PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
data = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", data);

if (size > 10)
size = 10;
printf("  first %ld bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02hhx", data[i]);
if (i < size - 1)
printf(" ");
}
printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
double value;
char *str_value;

if (!PyFloat_Check(p))
{
printf("[ERROR] Invalid Float Object\n");
return;
}

value = PyFloat_AsDouble(p);
str_value = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

printf("[.] float object info\n");
printf("  value: %s\n", str_value);

PyMem_Free(str_value);
}

