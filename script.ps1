function Set-Image
{
    $images_dir = $PSScriptRoot
    if (Test-Path $images_dir)
    {
        $images = Get-ChildItem $images_dir -Name
        if ($images.Count -eq 0)
        {
            echo "Folder is empty"
        }
        else
        {
            $images_dir = $PSScriptRoot + "\img"
            Set-Location $images_dir
            $images = Get-ChildItem $images_dir -Name
            $index = Get-Random -Maximum $images.Count
            $new_bg_image = $images_dir +'\' + $images[$index]
            reg query "HKCU\SOFTWARE\Microsoft\Internet Explorer\Desktop\General" /v WallpaperSource
            Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Internet Explorer\Desktop\General" -Name "WallpaperSource" -Value "$new_bg_image"
            echo "All done. Background image will be updated on next log on"
        }
    }
    else
    {
        New-Item $PSScriptRoot -Name "img" -ItemType "directory"
        echo "Load images in img folder and restart script..."
    }
}

function Check-Task
{
    schtasks.exe /query /fo list /tn "BG_CHANGER"
    cls
    return $LASTEXITCODE  
}

$is_scheduled = Check-Task
if ($is_scheduled -eq 1)
{
    cls
    echo "Add script to Task Scheduler..."
    schtasks /create /sc onlogon /rl highest /tn BG_CHANGER /tr D:\Visual_Studio_projects\bg_changer\script.ps1
    Set-Image
}
else
{
    cls
    echo "Scrip is already installed. Do you want to delete it? (y/n)"
    $input = Read-Host ">> "
    while ($input -ne 'y' -or $input -ne 'n')
    {
        if ($input -eq 'y')
        {
            schtasks /delete /tn BG_CHANGER
            echo "Script deleted from Task Scheduler"
            exit
        }
        elseif ($input -eq 'n')
        {
            exit
        }
        else
        { 
            echo "Wrong input!"
            $input = Read-Host ">> "
        }
    }
}