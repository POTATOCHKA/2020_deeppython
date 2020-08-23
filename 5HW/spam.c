#include <stdio.h>
#include <stdlib.h>

#include <Python.h>

PyObject* sample_sum(PyObject* self, PyObject* args)
{
	PyObject* list_obj;

	if (!PyArg_ParseTuple(args, "O", &list_obj)) {
		printf("ERROR: Failed to parse arguments");
		return NULL;
	}

	long len = PyList_Size(list_obj);

	printf("%ld", len);
	int mas[10];
	long res = 0;
	for (int i = 0; i < len; ++i)
	{
		PyObject* tmp = PyList_GetItem(list_obj, i);
		mas[i] = PyLong_AsLong(tmp) + 1;
	}

	return Py_BuildValue("O", *mas);
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
