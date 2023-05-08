from zipfile import ZipFile, ZIP_DEFLATED


def zip_file(files_paths: list, zip_path, password=None):
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as zipf:
        # Aggiungi i file da comprimere all'archivio
        for file_path in files_paths:
            zipf.write(file_path)
        # Setup the psw for the archive if exists
        if password:
            zipf.setpassword(password)

    # Aggiungi l'archivio zip come allegato
    with open(zip_path, "rb") as f:
        file_data = f.read()
        return file_data
