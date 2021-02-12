/*
    Testing file for EAL
*/

hook.Add("Initialize", "", function()
    print("%Test_Addon has loaded")
end)

concommand.Add("test_addon", function()
    print("%Test complete!")
end)