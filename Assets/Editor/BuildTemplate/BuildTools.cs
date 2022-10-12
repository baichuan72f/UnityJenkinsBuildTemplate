// BuildTools.cs

using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using UnityEngine;
using UnityEditor;

public class BuildTools
{
    [MenuItem("Build/Build APK")]
    public static void BuildApk()
    {
        // 解析参数
        using var reader = new StreamReader(Application.dataPath + "/Editor/BuildTemplate/arg.txt");
        var argStr = reader.ReadToEnd();
        Debug.Log(argStr);
        var reg = new Regex("[{].*[}]");
        var jsonStr = reg.Match(argStr).Value;
        Debug.Log(jsonStr);
        var arg = JsonConvert.DeserializeObject<JObject>(jsonStr);
        var paramList = new[] {"VERSION", "APPNAME", "VRPLATFORM", "BUNDLETYPE", "BUNDLEVERSION"};
        foreach (var item in paramList)
        {
            Debug.Log(LoadParam(arg, item));
        }

        PlayerSettings.bundleVersion = LoadParam(arg, "VERSION");
        PlayerSettings.productName = LoadParam(arg, "APPNAME");
        // 执行打包
        BuildPlayerOptions opt = new BuildPlayerOptions();
        opt.scenes = EditorBuildSettings.scenes.Where(s => s.enabled).Select(s => s.path).ToArray();
        opt.locationPathName = Application.dataPath + $"/../Bin/{PlayerSettings.productName}.apk";
        opt.target = BuildTarget.Android;
        opt.options = BuildOptions.None;
        BuildPipeline.BuildPlayer(opt);
        Debug.Log("Build App Done!");
    }

    static string LoadParam(JObject source, string path)
    {
        return source.SelectToken(path)?.Value<string>();
    }
}