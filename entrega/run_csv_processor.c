#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void run_python_script(const char *script, const char *arg1, const char *arg2, const char *arg3, const char *arg4) {
    // Estimativa inicial do tamanho do comando
    size_t command_size = strlen(script) + strlen(arg1) + strlen(arg2) + strlen(arg3) + strlen(arg4) + 50; // ajuste de tamanho
    char *command = malloc(command_size);

    if (!command) {
        perror("Falha ao alocar memória para comando");
        return;
    }

    //Formate a string de comando
    snprintf(command, command_size, "python3 %s \"%s\" \"%s\" \"%s\" \"%s\"", script, arg1, arg2, arg3, arg4);

    FILE *fp = popen(command, "r");
    if (fp == NULL) {
        perror("popen falhou");
        free(command);
        return;
    }



    //Abre um processo para executar o comando
    size_t buffer_size = 256 * 10; 
    char *buffer = malloc(buffer_size);
    if (!buffer) {
        perror("Failed to allocate memory for buffer");
        free(command);
        pclose(fp);
        return;
    }


    //Lê a saída linha por linha
    while (fgets(buffer, buffer_size, fp) != NULL) {

        size_t line_length = strlen(buffer);
        if (line_length == buffer_size - 1 && buffer[buffer_size - 2] != '\n') {
            //calculo do buffer para saída
            buffer_size *= 2;
            buffer = realloc(buffer, buffer_size);
            if (!buffer) {
                perror("Falha ao realocar memória para o buffer");
                free(command);
                pclose(fp);
                return;
            }
    
            fgets(buffer + line_length, buffer_size - line_length, fp);
        }

        // Print
        printf("%s", buffer);
    }

    
    free(command);
    free(buffer);
    if (pclose(fp) == -1) {
        perror("pclose failed");
    }

}

void processCsvFile(const char arg2[], const char arg3[], const char arg4[]) {
    const char script_name[] = "csv_processor.py";
    const char arg1[] = "file";
    run_python_script(script_name, arg1, arg2, arg3, arg4);
}

void processCsv(const char arg2[], const char arg3[], const char arg4[]) {
    const char script_name[] = "csv_processor.py";
    const char arg1[] = "data";
    run_python_script(script_name, arg1, arg2, arg3, arg4);
}
