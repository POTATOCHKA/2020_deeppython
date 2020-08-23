#include <stdio.h>
#include <stdlib.h>

#include <Python.h>

PyObject* sample_sum(PyObject* self, PyObject* args)
{
	PyObject* list_obj;
	long max_len;
	if (!PyArg_ParseTuple(args, "Ol", &list_obj, &max_len)) {
		printf("ERROR: Failed to parse arguments");
		return NULL;
	}
	long mas[10];
	long len = PyList_Size(list_obj);

	printf("DEBUG: length of list=%ld, max length=%ld\n", len, max_len);
	PyObject* l = PyList_New(max_len);
	long res = 0;
	for (int i = 0; i < len && i < max_len; ++i)
	{
		PyObject* tmp = PyList_GetItem(list_obj, i);
		res += PyLong_AsLong(tmp);
		PyList_SET_ITEM(l, i, PyInt_FromLong(tmp)+1);
	}
	for (int i=0; i<max_len; i++)
	{
		printf("%ld\n",mas[i]);
	}
	return l;
}

static PyMethodDef methods[] = {
	{ "sum", sample_sum, METH_VARARGS, "sum of elements of the list" },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef summodule = {
	PyModuleDef_HEAD_INIT, "sample_sum",
	NULL, -1, methods
};

PyMODINIT_FUNC PyInit_sample(void) {
	return PyModule_Create(&summodule);
}