-- Migration script for db_mahasiswa PostgreSQL database

-- Drop existing tables in correct order to prevent FK issues
DROP TABLE IF EXISTS matakuliah CASCADE;
DROP TABLE IF EXISTS kelas CASCADE;
DROP TABLE IF EXISTS mahasiswa CASCADE;

-- Create mahasiswa table
CREATE TABLE mahasiswa (
    "Id_mahasiswa" SERIAL PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    jurusan VARCHAR(255) NOT NULL,
    alamat TEXT,
    tahun_masuk INTEGER
);

-- Create kelas table
CREATE TABLE kelas (
    "Id_kelas" SERIAL PRIMARY KEY,
    semester VARCHAR(50) NOT NULL,
    "Id_mahasiswa" INTEGER,
    "Id_matakuliah" INTEGER,
    CONSTRAINT fk_mahasiswa_kelas FOREIGN KEY ("Id_mahasiswa") REFERENCES mahasiswa("Id_mahasiswa") ON DELETE SET NULL
);

-- Create matakuliah table
CREATE TABLE matakuliah (
    "Id_matakuliah" SERIAL PRIMARY KEY,
    nama_matakuliah VARCHAR(255) NOT NULL,
    jam_matakuliah INTEGER NOT NULL,
    "Id_kelas" INTEGER,
    "Id_mahasiswa" INTEGER,
    CONSTRAINT fk_kelas_matakuliah FOREIGN KEY ("Id_kelas") REFERENCES kelas("Id_kelas") ON DELETE SET NULL,
    CONSTRAINT fk_mahasiswa_matakuliah FOREIGN KEY ("Id_mahasiswa") REFERENCES mahasiswa("Id_mahasiswa") ON DELETE CASCADE
);

-- Add foreign keys to mahasiswa table after other tables are created
ALTER TABLE mahasiswa ADD COLUMN "Id_kelas" INTEGER;
ALTER TABLE mahasiswa ADD COLUMN "Id_matakuliah" INTEGER;
ALTER TABLE mahasiswa ADD CONSTRAINT fk_mahasiswa_kelas FOREIGN KEY ("Id_kelas") REFERENCES kelas("Id_kelas") ON DELETE SET NULL;
ALTER TABLE mahasiswa ADD CONSTRAINT fk_mahasiswa_matakuliah FOREIGN KEY ("Id_matakuliah") REFERENCES matakuliah("Id_matakuliah") ON DELETE SET NULL;

-- Optional: Indexes to speed up queries
CREATE INDEX idx_mahasiswa_kelas ON mahasiswa("Id_kelas");
CREATE INDEX idx_mahasiswa_matakuliah ON mahasiswa("Id_matakuliah");
CREATE INDEX idx_matakuliah_kelas ON matakuliah("Id_kelas");
CREATE INDEX idx_matakuliah_mahasiswa ON matakuliah("Id_mahasiswa");
