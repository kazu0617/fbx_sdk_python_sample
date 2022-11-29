import sys
from fbx import *

def main(obj_path, fbx_path, version_code):
    # Create
    manager = FbxManager.Create()
    scene = FbxScene.Create(manager, "fbxScene")
    importer = FbxImporter.Create(manager, "")
    exporter = FbxExporter.Create(manager, "")

    # Import the file to the scene
    importer.Initialize(obj_path, -1)
    importer.Import(scene)

    # Export the scene to the file.
    exporter.Initialize(fbx_path, -1)
    exporter.SetFileExportVersion(version_code, FbxSceneRenamer.eNone)
    exporter.Export(scene)

    # Destroy
    exporter.Destroy()
    importer.Destroy()
    scene.Destroy()
    manager.Destroy()


if __name__ == '__main__':
    # get argument
    args = sys.argv

    if len(args) < 2:
        print('Arguments are too short')
    elif len(args) == 3:
        main(args[1], args[2], 'FBX201200')
    elif len(args) > 3:
        main(args[1], args[2], args[3])
