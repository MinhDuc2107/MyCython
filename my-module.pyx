from libc.stdio cimport *
from libc.string cimport *
from libc.stdlib cimport *

from base64 import *

cdef class Open:
    cdef FILE *file
    cdef FILE *backup
    cdef bint close
    cdef bint cipher
    cdef bytes data
    cdef char*read

    def __init__(self, file = "file.txt", mode = "r", cipher = False):
        self.file = fopen(bytes(file, "UTF-8"), bytes(mode, "UTF-8"))
        self.read = <char*> calloc(9999999999, sizeof(char))
        self.data = b""
        self.close = True
        self.cipher = cipher

    cpdef void Write(self, string = "", base = "base64"):
        if not self.cipher:
            fprintf(self.file, "%s", bytes(string, "UTF-8"))
        elif self.cipher:
            if base == "base16":
                self.data = b16encode(string.encode("UTF-8"))
                fprintf(self.file, "%s", self.data)
            elif base == "base32":
                self.data = b32encode(string.encode("UTF-8"))
                fprintf(self.file, "%s", self.data)
            elif base == "base85":
                self.data = b85encode(string.encode("UTF-8"))
                fprintf(self.file, "%s", self.data)
            else:
                self.data = b64encode(string.encode("UTF-8"))
                fprintf(self.file, "%s", self.data)

    cpdef str Read(self, base = "base64"):
        fscanf(self.file, "%[^%s]", &self.read[0])
        if not self.cipher:
            self.data = &self.read[0]
            return str(self.data, "UTF-8")
        elif self.cipher:
            if base == "base16":
                self.data = b16decode(&self.read[0])
                return str(self.data, "UTF-8")
            elif base == "base32":
                self.data = b32decode(&self.read[0])
                return str(self.data, "UTF-8")
            elif base == "base85":
                self.data = b85decode(&self.read[0])
                return str(self.data, "UTF-8")
            else:
                self.data = b64decode(&self.read[0])
                return str(self.data, "UTF-8")

    cpdef Backup(self, link = ""):
        fscanf(self.file, "%[^%s]", &self.read[0])
        self.file = fopen(bytes(link + ".backup", "UTF-8"), b"w+")
        fprintf(self.file, "%s", &self.read[0])

    cpdef void Close(self):
        fclose(self.file)
        self.close = False

    def __str__(self):
        return f"I/O Text Version: 1.0"

    def __dealloc__(self):
        if self.close:
            fclose(self.file)
        free(self.read)
        remove(self.data)

cpdef public void Main():
    File = Open("file.text", "w+", True)
    File.Write("Có làm thì mới có ăn !!!")
    File = Open("file.text")
    File.Backup("/media/os/Mate/")

    File = Open("/media/os/Mate/.backup", "r", True)
    print(File.Read())



