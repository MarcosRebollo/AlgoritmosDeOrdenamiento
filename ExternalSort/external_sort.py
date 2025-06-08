import os
import shutil
import contextlib

class ExternalSort:
    def __init__(self, base_dir=None):
        """Initialize with base directory for temporary files"""
        self.base_dir = base_dir or os.path.dirname(os.path.abspath(__file__))
        self.temp_files = []
    
    def _create_temp_file(self, prefix):
        """Create a temporary file in the algorithm's directory"""
        temp_count = len(self.temp_files) + 1
        temp_path = os.path.join(self.base_dir, f'{prefix}_{temp_count}.txt')
        self.temp_files.append(temp_path)
        return temp_path
    
    def cleanup(self):
        """Clean up all temporary files"""
        for temp_file in self.temp_files:
            if os.path.exists(temp_file):
                try:
                    os.unlink(temp_file)
                except:
                    pass
        self.temp_files.clear()
    
    def _ensure_absolute_path(self, file_path):
        """Convert relative paths to absolute paths"""
        if not os.path.isabs(file_path):
            return os.path.join(self.base_dir, file_path)
        return file_path
    
    def merge_files(self, input_files, output_file):
        """Merge multiple sorted files into one sorted file"""
        output_path = self._ensure_absolute_path(output_file)
        open_files = []
        
        try:
            # Abrir todos los archivos de entrada
            for f_path in input_files:
                try:
                    f = open(self._ensure_absolute_path(f_path), 'r')
                    open_files.append(f)
                except Exception as e:
                    print(f"Error al abrir archivo {f_path}: {str(e)}")
                    raise
            
            with open(output_path, 'w') as out:
                values = []
                # Leer el primer valor de cada archivo
                for f in open_files:
                    line = f.readline().strip()
                    if line:
                        try:
                            values.append((float(line), f))
                        except ValueError:
                            print(f"Error al convertir línea: {line}")
                            raise
                
                # Usar min heap para mezclar
                while values:
                    min_val, min_file = min(values, key=lambda x: x[0])
                    out.write(f"{min_val:.1f}\n")
                    
                    # Leer siguiente valor del archivo que tenía el mínimo
                    line = min_file.readline().strip()
                    if line:
                        try:
                            values = [(float(line), min_file)] + [v for v in values if v[1] != min_file]
                        except ValueError:
                            print(f"Error al convertir línea: {line}")
                            raise
                    else:
                        values = [v for v in values if v[1] != min_file]
        
        finally:
            # Asegurar que todos los archivos se cierren
            for f in open_files:
                try:
                    f.close()
                except:
                    pass
