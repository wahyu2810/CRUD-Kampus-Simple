# TODO: Fix Foreign Key Constraint Error in Mahasiswa Creation

## Steps to Complete
- [x] Add imports for kelas and matakuliah repos in mahasiswa/usecase.py
- [x] Add validation in post method to check if Id_kelas exists in kelas table
- [x] Add validation in post method to check if Id_matakuliah exists in matakuliah table
- [x] Fix database schema to include Id_matakuliah in kelas table
- [x] Test the fix by attempting to create a mahasiswa with invalid Id_kelas
