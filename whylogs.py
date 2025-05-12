import whylogs as why
import pandas as pd

def dummy():
    print("Great Model!!!")

def main():
    titanic_df = pd.read_csv("data/titanic_data.csv")
    # separate the titanic_df into two using the Survived value for the purpose
    # of generating a drift summary
    # titanic profile
    titanic_profile = why.log(titanic_df)
    profile = titanic_profile.profile()
    prof_view = profile.view()
    # reference whylogs profile
    cond_reference = (titanic_df['Survived']==0)
    titanic_reference = titanic_df.loc[cond_reference]
    # drop the Survived and Name columns
    titanic_reference = titanic_reference.drop(["Survived","Name"], axis=1)
    ref_result = why.log(pandas=titanic_reference)
    ref_prof_view = ref_result.view()
    # target whylogs profile
    cond_target = (titanic_df['Survived']==1)
    titanic_target = titanic_df.loc[cond_target]
    # drop the Survived and Name columns
    titanic_target = titanic_target.drop(["Survived","Name"], axis=1)
    target_result = why.log(pandas=titanic_target)
    target_prof_view = target_result.view()
    # instantiate NotebookProfileVisualizer to generate report
    from whylogs.viz import NotebookProfileVisualizer

    visualization = NotebookProfileVisualizer()
    visualization.set_profiles(target_profile_view=target_prof_view, reference_profile_view=ref_prof_view)
    # # generate drift report
    visualization.summary_drift_report()



if __name__ == '__main__':
    dummy()
