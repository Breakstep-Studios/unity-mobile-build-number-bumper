from unityparser import UnityDocument


def run():
    project_settings_file_path = 'ProjectSettings/ProjectSettings.asset'
    unity_document = UnityDocument.load_yaml(project_settings_file_path)
    projectsettings_monobehaviour_document = unity_document.entry

    try:
        android_build_number = projectsettings_monobehaviour_document.AndroidBundleVersionCode
    except AttributeError:
        print("Failed to find AndroidBundleVersionCode in ProjectSettings.asset")
        return
    try:
        ios_build_number = projectsettings_monobehaviour_document.buildNumber["iPhone"]
    except AttributeError:
        print("Failed to find buildNumber.iPhone in ProjectSettings.asset")
        return

    old_android_build_number = android_build_number
    old_ios_build_number = ios_build_number
    android_build_number += 1
    ios_build_number += 1

    print("AndroidBundleVersionCode: " + str(old_android_build_number) + " -> " + str(android_build_number))
    print("iOS Build Number: " + str(old_ios_build_number) + " -> " + str(ios_build_number))

    projectsettings_monobehaviour_document.AndroidBundleVersionCode = android_build_number
    projectsettings_monobehaviour_document.buildNumber["iPhone"] = ios_build_number

    # see https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-output-parameter
    print(f"::set-output name=android-build-number-before::{old_android_build_number}")
    print(f"::set-output name=android-build-number-after::{android_build_number}")
    print(f"::set-output name=ios-build-number-before::{old_ios_build_number}")
    print(f"::set-output name=ios-build-number-after::{ios_build_number}")
    unity_document.dump_yaml()
    return


run()
