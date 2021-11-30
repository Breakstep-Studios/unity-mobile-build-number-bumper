from unityparser import UnityDocument


def run():
    project_settings_file_path = './ProjectsSettings/ProjectsSettings.asset'
    unity_document = UnityDocument.load_yaml(project_settings_file_path)
    projectsettings_monobehaviour_document = unity_document.entry

    try:
        version = projectsettings_monobehaviour_document.AndroidBundleVersionCode
    except AttributeError:
        print("Failed to find photonNetworkVersion in NetworkConfig.asset")
        return

    old_networking_version = version
    version += 1
    print(str(old_networking_version) + " -> " + str(version))
    projectsettings_monobehaviour_document.photonNetworkingVersion = version
    # see https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-output-parameter
    print(f"::set-output name=new-build-number::{version}")
    unity_document.dump_yaml()
    return


run()