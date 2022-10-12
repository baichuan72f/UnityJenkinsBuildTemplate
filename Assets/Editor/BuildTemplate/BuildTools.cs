// BuildTools.cs
using UnityEngine;
using UnityEditor;

public class BuildTools
{
    [MenuItem("Build/Build APK")]
    public static void BuildApk()
    {
        // 解析参数
        using var reader = new TextReader();
         PlayerSettings.bundleVersion = "1.0.0";
        PlayerSettings.productName = "test";
        // 执行打包
        BuildPlayerOptions opt = new BuildPlayerOptions();
        opt.scenes = new string[] { "Assets/Scenes/SampleScene.unity" };
        opt.locationPathName = Application.dataPath + $"/../Bin/{PlayerSettings.productName}.apk";
        opt.target = BuildTarget.Android;
        opt.options = BuildOptions.None;

        BuildPipeline.BuildPlayer(opt);

        Debug.Log("Build App Done!");
    }
}
