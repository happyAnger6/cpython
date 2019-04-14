#include "Python.h"
#include "sample.h"

#ifdef __cplusplus
extern "C" {
}
#endif

typedef struct {
    Point *(*aspoint)(PyObject *);
    PyObject *(*frompoint)(Point *,int);
}_PointAPIMethods;

#ifndef PYSAMPLE_MODULE
static _PointAPIMethods *_point_api = 0;

static int import_sample(void) {
    _point_api = (_PointAPIMethods *)PyCapsule_Import("sample._point_api", 0);
    return (_point_api != NULL)? 1 : 0;
}