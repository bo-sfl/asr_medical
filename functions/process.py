from werkzeug import secure_filename
from azure.storage.blob import BlockBlobService


ALLOWED_EXTENSIONS = {'wav'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_format(audio):
    """ check that the file format is correct """
    if audio and allowed_file(audio.filename):
        return 1
    else:
        return 0

def save_to_bucket(audio):
    output = audio.save(secure_filename(audio.filename))
    save_name = secure_filename(audio.filename)

    accountName = "all2sflminiproject"
    # For ecurity, need to create vault, register function (or app?) in active directory,
    #and retrieve key from vault
    accountKey = "gKaFO2TRDXMzVT50JTeWgeNCxR529Rj173/CeknKM70T/Y13T05zKdxXaziqPUfLUramRgyZkBQ9m8VQtI5RcQ=="
    containerName = "raw8audio"
    # blobName = "***"
    blob_file_name = save_name

    block_blob_service = BlockBlobService(account_name=accountName, account_key=accountKey)

    block_blob_service.create_blob_from_bytes(containerName, blob_file_name, audio.read())

    return


# def convert_for_asr(audio):
    # containerName = "raw8audio"
    # blob_file_name = secure_filename(audio.filename)
    # accountName = "all2sflminiproject"
    # accountKey = "MKNsD3qP0Gf5FLjjzalOq/HU9k1NBY1Ys1g16hFht11SBbToiduOQ3w686VPBDqXOSXhrrHpbJ4Iw/IrGyVXuQ=="
    #
    # block_blob_service = BlockBlobService(account_name=accountName, account_key=accountKey)
    # raw = block_blob_service.get_blob_to_bytes(containerName, blob_file_name, 'out-sunset
    #
    # y = librosa.to_mono(audio.read())                            # convert to monochannel
    # sf.write(path, format='wav', data=data, samplerate=16000)  # save at 16 kHz
    # return
