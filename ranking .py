import pandas as pd
data=pd.read_csv("Cricket_Raw.csv")
data["Player_Name"]=data["Player_Name"].str.strip()
data["Role"]=data["Role"].str.strip()
#Calculation
data["Average"]=0
data["Strike_Rate"]=0
data["Economy"]=0
data["Average"]=(data["Runs"]/(data["Outs"]).replace(0,1)).round(2)
data["Strike_Rate"]=((data["Runs"]/(data["Balls_Faced"].replace(0,1)))*100).round(2)
data["Economy"]=(data["Runs_Conceded"]/(data["Balls_Bowled"]/6).replace(0,1)).round(2)
data.to_csv("Cricket_Final.csv",index=False)
#Batsmen sorting
Batsmen_df=data[data["Role"]=="Batsman"].copy()
Batsmen_df=Batsmen_df.sort_values(by=["Runs","Average"],ascending=False)
Batsmen_df["Rank"] = range(1, len(Batsmen_df) + 1)
Batsmen_df.to_csv("Batsmen_Leaderboard.csv", index=False)
#Bowler sorting
Bowlers_df = data[data["Role"] == "Bowler"].copy()
Bowlers_df = Bowlers_df.sort_values(by=["Wickets", "Economy"], ascending=[False, True])
Bowlers_df["Rank"] = range(1, len(Bowlers_df) + 1)
Bowlers_df.to_csv("Bowlers_Leaderboard.csv", index=False)
#All rounder sorting
AR_df = data[data["Role"] == "All-Rounder"].copy()
AR_df = AR_df.sort_values(by=["Wickets", "Runs"], ascending=False)
AR_df["Rank"] = range(1, len(AR_df) + 1)
AR_df.to_csv("AllRounder_Leaderboard.csv", index=False)  
        
    
        
    
    
    
    
    
