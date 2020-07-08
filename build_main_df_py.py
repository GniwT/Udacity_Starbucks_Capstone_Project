# Create function to combine transaction, offer, portfolio and profile datasets

import numpy as np
import pandas as pd

def to_build_main_df(clean_portfolio, clean_profile, offers_df, trans_df):
    
    
    '''Create a combined dataframe from the transaction, demographic and offer data:
    INPUT:
        portfolio - (dataframe),offer metadata
        profile - (dataframe),customer demographic data
        offers_df - (dataframe), offers data for customers
        transaction_df - (dataframe), transaction data for customers
    OUTPUT:
        combined_data_df - (dataframe),combined data from transaction, demographic and offer data
    '''
    
    base_df = [] # Initialize empty list for combined data
    cust_id_ls = trans_df['customer_id'].unique().tolist() # List of unique customers in offers_df
        

    # Iterate over each customer
    for i,cust_id in enumerate(cust_id_ls):
            
        # select customer profile from profile data
        #cust_profile = clean_profile[clean_profile['customer_id'] == cust_id] 
        
        # select offers associated with the customer from offers_df
        cust_offer = offers_df[offers_df['customer_id'] == cust_id]
        
        # select transactions associated with the customer from transactions_df
        cust_trans = trans_df[trans_df['customer_id'] == cust_id]
        
        # select received, completed, viewed offer data from customer offers
        offer_recd  = cust_offer[cust_offer['offer_received'] == 1]
        offer_viewed = cust_offer[cust_offer['offer_viewed'] == 1]
        offer_comp = cust_offer[cust_offer['offer_completed'] == 1]
            
        # Iterate over each offer received by a customer
        rows = [] # Initialize empty list for a customer records
            
        for off_id in offer_recd['offer_id'].values.tolist():
            
            # select duration of a particular offer_id
            offer_duration = clean_portfolio.loc[clean_portfolio['offer_id'] == off_id, 'duration'].values[0]
            
            # select the time when offer was received
            offer_recd_time = offer_recd.loc[offer_recd['offer_id'] == off_id, 'time'].values[0]
            
            # Calculate the time when the offer ends
            offer_end_time = offer_recd_time + offer_duration
            
            #Initialize a boolean array that determines if the customer viewed an offer between offer period
            valid_viewed = np.logical_and(offer_viewed['time'] >= offer_recd_time, offer_viewed['time'] <= offer_end_time)
                
            # Check if the offer type is 'bogo' or 'discount'
            if (clean_portfolio[clean_portfolio['offer_id'] == off_id]['bogo'].values[0] == 1 or\
                    clean_portfolio[clean_portfolio['offer_id'] == off_id]['discount'].values[0] == 1):
                
                #Initialize a boolean array that determines if the customer completed an offer between offer period
                offers_comp = np.logical_and(offer_comp['time'] >= offer_recd_time, offer_comp['time'] <= offer_end_time)
                    
                #Initialize a boolean array that selects customer transctions between offer period
                valid_tran = cust_trans[np.logical_and(cust_trans['time'] >= offer_recd_time, 
                                                           cust_trans['time'] <= offer_end_time)]
                    
                # Determine if the customer responded to an offer(bogo or discount) or not
                cust_action = np.logical_and(valid_viewed.sum() > 0, offers_comp.sum() > 0) and\
                                                    (valid_trans['amount'].sum() >=\
                                                     clean_portfolio[clean_portfolio['offer_id'] == off_id]['difficulty'].values[0])
                
            # Check if the offer type is 'informational'
            elif clean_portfolio[clean_portfolio['offer_id'] == off_id]['informational'].values[0] == 1:
                
                #Initialize a boolean array that determines if the customer made any transctions between offer period
                cust_info_tran = np.logical_and(cust_trans['time'] >= offer_recd_time, cust_trans['time'] <= offer_end_time)                   
                    
                # Determine if the customer responded to an offer(informational) or not
                cust_action = valid_viewed.sum() > 0 and cust_info_tran.sum() > 0                  
                
                #Initialize a boolean array that selects customer transctions between offer period
                valid_trans = cust_trans[np.logical_and(cust_trans['time'] >= offer_recd_time, 
                                                        cust_trans['time'] <= offer_end_time)]
                
            # Initialize a dictionary for a customer with required information for a particular offer
            cust_action_ls = {'cust_action': int(cust_action),'time': offer_recd_time,'total_amount': valid_trans['amount'].sum()}
            #cust_action_ls = {'cust_action': int(cust_action),'time': offer_recd_time,'total_amount': valid_trans['amount']}
            cust_action_ls.update(clean_profile[clean_profile['customer_id'] == cust_id].squeeze().to_dict())
            cust_action_ls.update(clean_portfolio[clean_portfolio['offer_id'] == off_id].squeeze().to_dict())
                
            # Add the dictionary to list for combined_data
            rows.append(cust_action_ls)
            
        # Add the dictionaries from rows list to combined_data list
        base_df.extend(rows)
            
        
    # Convert combined_data list to dataframe
    main_df = pd.DataFrame(base_df)
    
    return main_df