#!/usr/bin/env python3
import intune
import dell
import files


def main ():
    app = intune.Create_Client_Application_Instance()
    
    token = intune.Create_Token(app=app)
    intune.Test_Token(token)
    
    access = intune.Create_Access(token_response=token)
    headers = intune.Create_Headers(access_token=access)
    
    devices = intune.Fetch_Devices(headers=headers)
    intune.Count_Devices(devices=devices)
    
    dataframe = intune.Convert_List_To_DataFrame(devices=devices)
    
    breakdownFile = files.Access_BreakDown_CSV("breakdowns.csv")
    files.Read_BreakDowns(breakdownFile, dataframe)
    

if __name__ == "__main__":
    main()