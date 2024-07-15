#include <stdio.h>
#include <dlfcn.h>

int main() {

    const char arg2[] = "data.csv";
    const char arg3[] = "header1,header3";
    const char arg4[] = "header1>1 and header3<8";


    const char arg2_data[] = "header1,header2,header3\n1,2,3\n4,5,6\n7,8,9";
    const char arg3_data[] = "header1,header3";
    const char arg4_data[] = "header1>1 and header3<8";



    //Carrega a biblioteca compartilhada
    void *handle = dlopen("./libcsv.so", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "Cannot open library: %s\n", dlerror());
        return 1;
    }


    void (*processCsvFile)(const char*, const char*, const char*) = dlsym(handle, "processCsvFile");
    if (!processCsvFile) {
        fprintf(stderr, "Cannot load symbol 'processCsvFile': %s\n", dlerror());
        dlclose(handle);
        return 1;
    }

    void (*processCsv)(const char*, const char*, const char*) = dlsym(handle, "processCsv");
    if (!processCsv) {
        fprintf(stderr, "Cannot load symbol 'processCsv': %s\n", dlerror());
        dlclose(handle);
        return 1;
    }

    //Chama as funções com parâmetros
    processCsvFile(arg2, arg3, arg4);
    processCsv(arg2_data, arg3_data, arg4_data);

    //Fecha a biblioteca compartilhada
    dlclose(handle);
    return 0;
}
