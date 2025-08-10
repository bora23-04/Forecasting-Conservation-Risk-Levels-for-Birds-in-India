import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px


# Load model + target encoder
model = joblib.load('bird_conservation_model5.pkl')
target_encoder = joblib.load('target_encoders5.pkl')  # Must be LabelEncoder trained on ['Low', 'Medium', 'High']

# Load dataset for dropdowns and EDA
birds_df = pd.read_excel("my_data.xlsx", engine='openpyxl')



st.set_page_config(page_title="Bird Conservation Predictor", layout="wide")
st.title("🦜 Bird Conservation Concern Predictor")

# -------- SIDEBAR input form --------
st.sidebar.header("Input Bird Traits")

group = st.sidebar.multiselect("Group", birds_df['group'].unique())
iucn = st.sidebar.selectbox("IUCN Status", birds_df['iucn_status'].unique())
wlpa = st.sidebar.selectbox("WLPA Schedule", birds_df['wlpa_schedule'].unique())

anal_long = st.sidebar.number_input("Analysed Long-Term", min_value=0, max_value=1000, value=0)
anal_curr = st.sidebar.number_input("Analysed Current", min_value=0, max_value=1000, value=0)

long_trend = st.sidebar.slider("Long-Term Trend (%)", -100.0, 200.0, 0.0)
curr_change = st.sidebar.slider("Current Annual Change (%)", -50.0, 200.0, 0.0)

long_term_status = st.sidebar.selectbox("Long-Term Status", birds_df['long_term_status'].unique())
current_status = st.sidebar.selectbox("Current Status", birds_df['current_status'].unique())
distribution_status = st.sidebar.selectbox("Distribution Status", birds_df['distribution_status'].unique())

migration = st.sidebar.multiselect("Migratory Status", birds_df['migratory_status'].unique())
diet = st.sidebar.selectbox("Diet", birds_df['diet'].unique())
habitat = st.sidebar.selectbox("Habitat Type", birds_df['habitat_type'].unique())
endemic = st.sidebar.selectbox("Endemicity Type", birds_df['endemicity_type'].unique())
bird_type = st.sidebar.selectbox("Bird Type", birds_df['bird_type'].unique())

# Input dict
input_dict = {
    "group": ",".join(group) if isinstance(group, list) else group,
    "migratory_status": ",".join(migration) if isinstance(migration, list) else migration,
    "diet": diet,
    "habitat_type": habitat,
    "wlpa_schedule": wlpa,
    "iucn_status": iucn,
    "analysed_long_term": anal_long,
    "analysed_current": anal_curr,
    "long_term_trend": long_trend,
    "current_annual_change": curr_change,
    "long_term_status": long_term_status,
    "current_status": current_status,
    "distribution_status": distribution_status,
    "endemicity_type": endemic,
    "bird_type": bird_type
}

# -------------- Predict --------------
if st.button("Predict Conservation Concern"):
    input_df = pd.DataFrame([input_dict])
    # Predict encoded label (0,1,2)
    pred_encoded = model.predict(input_df)[0]

    # Convert it back to label (Low, Moderate, High)
    pred_label = target_encoder.inverse_transform([pred_encoded])[0]

    # Get probabilities and map to readable labels
   # probs = model.predict_proba(input_df)[0]
   # prob_dict = {
    #    target_encoder.inverse_transform([i])[0]: float(prob)
     #   for i, prob in enumerate(probs)
    #}

    st.success(f"Predicted Conservation Concern: *{pred_label}*")
   # st.write("Prediction Probabilities:", prob_dict)

# -------------- EDA PLOTS --------------
state = st.sidebar.multiselect("State", birds_df.columns[19:], help="State columns")

df = birds_df.copy()
if group:
    df = df[df['group'].isin(group)]
if migration:
    df = df[df['migratory_status'].isin(migration)]
if state:
    df = df[df[state].sum(axis=1) > 0]

# ----------- CHART BLOCK 1 -----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("IUCN Status split")
    pie1 = px.pie(df, names='iucn_status')
    st.plotly_chart(pie1, use_container_width=True)

    with st.expander("📄 View Data"):
        tab = df['iucn_status'].value_counts().reset_index()
        st.table(tab)
        csv = tab.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "iucn_split.csv", "text/csv")

with col2:
    st.subheader("Migratory Status split")
    pie2 = px.pie(df, names='migratory_status')
    st.plotly_chart(pie2, use_container_width=True)

    with st.expander("📄 View Data"):
        tab = df['migratory_status'].value_counts().reset_index()
        st.table(tab)
        csv = tab.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "migration_split.csv", "text/csv")

# ----------- CHART BLOCK 2 -----------
col3, col4 = st.columns(2)

with col3:
    st.subheader("Diet vs Bird Type")
    cross = pd.crosstab(df['diet'], df['bird_type']).reset_index()
    fig = px.bar(cross, x='diet', y=[c for c in cross.columns if c != 'diet'], barmode='stack')
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📄 View Data"):
        st.table(cross)
        csv = cross.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "diet_birdtype.csv", "text/csv")

with col4:
    st.subheader("Top 10 Threatened States")
    bad_cols = ['analysed_current', 'analysed_long_term']
    state_cols = [c for c in df.select_dtypes(include='int64').columns if c not in bad_cols]
    threat_df = df[df['status_of_conservation_concern'] != 'Low']
    state_rank = pd.Series({s: threat_df[s].sum() for s in state_cols}).sort_values(ascending=False).head(10)
    top_df = pd.DataFrame({'State': state_rank.index, 'Threatened Count': state_rank.values})
    fig2 = px.bar(top_df, x='State', y='Threatened Count', color='Threatened Count')
    st.plotly_chart(fig2, use_container_width=True)

    with st.expander("📄 View Data"):
        st.table(top_df)
        csv = top_df.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "top_10_states.csv", "text/csv")


st.subheader("Top 10 Bird Groups vs IUCN Status")
group_iucn_ct = pd.crosstab(birds_df['group'], birds_df['iucn_status'])
top_groups = group_iucn_ct.sum(axis=1).sort_values(ascending=False).head(10).index
filtered_ct = group_iucn_ct.loc[top_groups]
plot_df = filtered_ct.reset_index().melt(id_vars='group', var_name='iucn_status', value_name='count')

fig3 = px.bar(plot_df, x='group', y='count', color='iucn_status', barmode='group')
fig3.update_layout(xaxis_title='Bird Group', yaxis_title='Count', xaxis_tickangle=45)
st.plotly_chart(fig3, use_container_width=True)
with st.expander("📄 View Summary Table"):
    st.table(plot_df)
    csv_data = plot_df.to_csv(index=False).encode()
    st.download_button("Download CSV", data=csv_data, file_name="group_vs_iucn.csv", mime="text/csv")