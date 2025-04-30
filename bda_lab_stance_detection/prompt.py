
# System prompts for specific tasks
SYSTEM_PROMPTS = {
    'STANCE_DETECTION_LM': """You are an expert in natural language processing and stance
detection. Your task is to analyze X post about Luigi Mangione and identify the associated
stance of the writer of each post."""
    ,
    'STANCE_DETECTION_BT': """You are an expert in natural language processing and stance detection. 
Your task is to analyze X post about Brian Thompson and identify the associated stance of 
the writer of each post."""
    ,
    'STANCE_DETECTION_UHC': """You are an expert in natural language processing and stance 
detection. Your task is to analyze X post about UnitedHealth and other Health insurance 
companies and identify the associated stance of the writer of each post."""
}

# Detailed prompts for specific tasks
TASK_PROMPTS = {
    'LUIGI_PROMPT': """
# BACKGROUND: 
Luigi Nicholas Mangione, born May 6, 1998, is an American man who was identified as the suspect 
in the killing of Brian Thompson, the CEO of UnitedHealthcare, which took place in New York City on December 4, 2024. 
Mangione was arrested and arraigned in Altoona, Pennsylvania five days after the shooting. He is referred to as the UHC
assassin, the UHC murder suspect, the CEO killer, and other monikers.

# TASK: 
Here is one X post about Luigi Mangione related to the event above. Please classify the stance of 
each post into one of the following categories: In Favor, Against, or Neutral.

STANCE_DICT = {{ -1: "Against", 0: "Neutral", 1: "In-Favor"}}

# INSTRUCTIONS:
1. The definition of "In-Favor" of Luigi Mangione:
    - Expresses approval, support, or praise for Luigi Mangione, or his actions or appearance.
    - Shows empathy toward Luigi Mangione (e.g., well-wishing or prayers for him).
    - Highlights perceived successes, achievements, or positive outcomes of his actions.
    - Clear demonstration of positive stance against Luigi Mangione (or reference to "CEO shooter" etc.) is required.

2. The definition of "Against" Luigi Mangione:
    - Expresses disapproval, criticism, or opposition to Luigi, his actions, or environments.
    - Highlights perceived failures, negative consequences, or harmful outcomes of his actions.
    - Clear demonstration of negative stance against Luigi Mangione is required.

3. The definition of "Neutral" to Luigi Mangione:
    - Presents mixed or conflicting stance, balancing both in favor and against aspects without leaning toward either side.
    - Discusses topics unrelated to Luigi Mangione's persona, actions, or appearance.
    - Does not mention or reference Luigi Mangione.
    - Mentions Luigi but it is about Nintendo games and their characters.
    - Luigi Mangione is mentioned but the stance is unclear.
    - May include In-Favor or Against only based on extended contextual knowledge.
    - Reference to objective reporting of Luigi Mangione (e.g. "was charged with murder").

4. Some posts might include multiple stances. Please focus on the overall stance toward Luigi Mangione and choose the most dominant stance.

# EXAMPLES:
    ## Examples of In-Favor Post:
    - "I love Luigi Mangione!"
    - "They keep trying to make Luigi Mangione look bad but instead he looks like NPH in that one episode where he looks great in every picture"
    - "Shooter's a hero. I wonder how many people died because of Brian Thompson's company?"
    - "Mangione is a hero"
    - "People will only care about your death if you're a rich white man. Free Luigi Mangione"
    - "Here's to you Luigi Mangione" does fit the cadence
    - "Has Luigi Mangione been pardoned yet?"

    ## Examples of Against Post:
    - "He's talking about Luigi murdering United healthcare CEO. You think this guy Luigi is a hero?"
    - "I don't like CEOs. Nor do I like Luigi."
    - "i haven't said anything about that Luigi case because i wanted all the facts and now that I have them. 
        Why people are gunning for a MURDERER to be free is insane to me! He killed a man that had a family, the healthcare system is still messed up like.."
    - "Murder is bad. Killing people is bad. Luigi Mangione is not a hero and should face justice for his actions. 
        Brian Thompson was a terrible person who ran an evil company responsible for the deaths and suffering of many many people
        and deserves no sympathy whatsoever."
    - "Luigi Mangione: - Elite high school & college education (IQ undoubtedly high). - Couldn't
        crack it in America (skills issue). - Takes anger at society out on the CEO Brian Thompson
        (a good man by all accounts). - This has everything to do with Luigi's personal
        shortcomings.…"
    - "Kyle is a hero. Luigi is a murderer"
    - "When all the weirdos scream 'Free Luigi,' they need to ensure no one, in fact, frees Luigi. Do you really not get it? Really???"
    - "They say Luigi Mangione was radicalized in Hawaii. Hmm"
    - "No ladies, you cannot fix Luigi Mangione."
    - "Luigi Mangione Suffered Chronic Back Pain, Friends Say He Fell Out Of Touch Earlier This Year"

    ## Examples of Neutral Posts:
    - "I feel like there's some real tension in following 'violence is never the answer' with 
        'people can only be pushed so far.' Violence is either acceptable in politics or it isn't."
    - "The suspected killer of the United Healthcare CEO, Brian Thompson, was found in a McDonald's in Pennsylvania yesterday. 
        He has been identified as 26-year-old Luigi Mangione."
    - After seeing that AI project Brian Thompson was heading up, I can easily see why he got
        clapped. That AI program was rejecting an additional 90 percent of cases from what they are saying. Sheesh
    - "UnitedHealth issued a statement after the arrest of a person of interest in murder of CEO Brian Thompson, 
        saying, 'our hope' is the arrest brings "some relief to Brian's family, friends, colleagues and the many others
        affected by this unspeakable tragedy"
    - "Luigi Mangione was charged with murder."
    - "UnitedHealthcare CEO Shooter Lookalike Competition!"
    - "Luigi Mangione was not insured by United Health Care. But his mother was. Something is wrong with the hole thing. I wonder who paid him.
    - "Luigi seduced the ajhummas, it's so over"
    - "charge them with terrorism instead of luigi"
    - "Why are Luigi and his lawyer in twinsie outfits?"

    
Now classify the stance regarding Luigi Mangione in the following X post. Using the STANCE_DICT, ONLY output the numeric value for the stance

{text}

# FORMATTING:
1. Please only provide a label for each post (1, -1, or 0).
2. Do not include any additional information or context.
3. You will be given a great penalty if you provide redundant information or context.
"""
,

'BRIAN_PROMPT' : """
# Background: On December 4, 2024, Brian Robert Thompson, the CEO of the US health insurance company UnitedHealthcare,
was shot in the back and killed in Midtown Manhattan, New York City. On December 9, 2024, authorities arrested 26-year-old 
Luigi Mangione in Altoona, Pennsylvania, and charged him in a Manhattan court with Thompson's killing.  

He is referred to as the UHC CEO, the CEO, and other monikers. 

# Task: 
Here is one X post about Brian Thompson related to the event above. Please classify the stance of each post into one of the following categories: In Favor, Against, or Neutral. 

STANCE_DICT = {{ -1: "Against", 0: "Neutral", 1: "In-Favor"}}

Instructions: 
1. The definition of In-Favor of Brian Thompson: 
·        Expresses approval, support, or praise for Brian Thompson or his Legacy 
·        Shows empathy toward Brian Thompson (e.g., well-wishing or prayers for him). 
·        Expresses condolences to the Thompson family or highlights Thompson’s role as a father 
·        Highlights perceived successes, achievements, or positive outcomes of his actions 
·        Clear demonstration of positive stance towards Brian Thompson (or reference to UHC CEO, etc.) is required. 

2. The definition of Against Brian Thompson: 
·        Expresses disapproval, criticism, or opposition to Thompson, his actions, or environments. 
·        Highlights perceived failures, negative consequences, or harmful outcomes of his actions. 
·        Clear demonstration of negative stance against Brian Thompson is required. 

3. The definition of Neutral to Brian Thompson: 
·        Presents mixed or conflicting stance, balancing both in favor and against aspects without leaning toward either side. 
·        Discusses topics unrelated to Brian Thompson’s persona, actions, or legacy. 
·        Does not mention or reference Brian Thompson. 
·        Mentions Brian or Thompson but it is clear it is not talking about the UHC CEO Brian Thompson 
·        Brian Thompson is mentioned but the stance is unclear. 
·        May include In-Favor or Against only based on extended contextual knowledge. 
-     Reference to objective reporting of Brian Thompson (e.g. “was killed in Midtown.”). 

4. Some posts might include multiple stances. Please focus on the overall stance toward Brian Thompson and choose the most dominant stance. 

# Examples 
    ## In-Favor Post: 
        “RT @RashidKhan1515 @kaitlancollins This incident has shocked those familiar with Thompson's career, marking a somber moment not only for UnitedHealthcare but for the broader business community, given his prominent role in the healthcare industry.” 
        “RT @DanMcIntyre5 @ArmandDoma Brian Thompson was from a small town in Iowa of 1200 people and graduated with a BS Biz & Accounting degree from the U of Iowa. He literally just worked his way up the corporate ladder. He lived in a mostly middle class suburb and his kids go to a public school.” 
        “Luigi Mangione: - Elite high school & college education (IQ undoubtedly high). - Couldn’t crack it in America (skills issue). - Takes anger at society out on the CEO Brian Thompson (a good man by all accounts). - This has everything to do with Luigi’s personal shortcomings.…” 
        “RT @QuakerNana United Healthcare CEO Brian Thompson was murdered today. Murder is ALWAYS wrong. Holding his family in The Light. What does not make news are the THOUSANDS of Americans who die because their health claim was denied by insurance companies. https://t.co/DHgQ3tdTuQ https://t.co/pdj7ozfSKj” 

    ## Against Post: 
        ““Murder is bad. Killing people is bad. Luigi Mangione is not a hero and should face justice for his actions. Brian Thompson was a terrible person who ran an evil company responsible for the deaths and suffering of many many people and deserves no sympathy whatsoever.” 
        “Luigi Mangione, you’re a hero. Fuck this system. Fuck Brian Thompson. Fuck this healthcare system.” 
        “@ShadowofEzra ◾While Brian Thompson was CEO of United Health Care, the company began using Al to automate the denial of services. The Al was found to have a 90% error rate, but the company continued to use it, resulting in millions of people being denied medically-necessary and lifesaving…” 
        “They sure did, in every way possible. Also, I wouldn't say this murder was "coldblooded." Coldblooded is denying cancer patients care so you can buy a second home. Fuck Brian Thompson. Fuck privatizing healthcare. Fuck all of the greedy people...and fuck Elon Musk twice.” 
        “After seeing that AI project Brian Thompson was heading up, I can easily see why he got clapped. That AI program was rejecting an additional 90% of cases from what they are saying. Sheesh” 
        “@CBSNews Under Brian Thompson, CEO of UnitedHealthcare leadership, the company used artificial intelligence to deny medical care, resulting in thousands of deaths annually. It is estimated that these refusals contributed to more than 60,000 deaths per year!!!😡” 

    ## Neutral Posts: 
        “@ignoramus02 He's the assassin of CEO Brian Thompson. But people are following him like a superhero... that's just crazy! https://t.co/FJNX1sjKld” 
        “@teameffujoe ok, but who gets to decide who the bad guy is? Most people didn't even know who Brian Thompson was until he was killed, and all of a sudden we know enough about him to call him the bad guy?” 
        “Huge new lead in Brian Thompson assassination as suspect is detained with trove of chilling evidence https://t.co/OlKjV3pcbf via https://t.co/IZ0loEIVD4” 
        “Something is fishy with that Brian Thompson story.” 

 
Now Classify the stance regarding Brian Thompson in the following X post. Using the STANCE_DICT, output the numeric key for the stance 

{text}

# FORMATTING:
1. Please only provide a label for each post (1, -1, or 0).
2. Do not include any additional information or context.
3. You will be given a great penalty if you provide redundant information or context.
"""
,
'UHC_PROMPT' : """
# Background: 
UnitedHealth Group Incorporated is an American multinational for-profit company specializing in health insurance and health 
care services. Selling insurance products under UnitedHealthcare, and health care services under the Optum brand, it is the world's 
ninth-largest company by revenue and the largest health care company by revenue. On December 4, 2024, UnitedHealthcares’s CEO, Brain Thompson, 
was shot in the back and killed in Midtown Manhattan. Relevant terms for this analysis will be referred to as UnitedHealth, UnitedHealthcare, UHC, and other monikers. 

# Task: 
Here is one X post about UnitedHealth or other health insurance companies related to the event above. 
Please classify the stance of each post into one of the following categories: In Favor, Against, or Neutral. 

STANCE_DICT = {{ -1: "Against", 0: "Neutral", 1: "In-Favor"}} 

Instructions: 
1. The definition of In-Favor of UnitedHealth or US Healthcare Insurance companies: 
    - Expresses approval, support, or praise for UnitedHealth or US Healthcare Insurance companies 
    - Highlights perceived successes, strengths, or positive aspects of UnitedHealth or US Healthcare Insurance companies 
    - Shares experiences where UnitedHealth or US Healthcare Insurance companies aided the writer through hardship 
    - Clear demonstration of positive stance towards UnitedHealth or US Healthcare Insurance companies (or reference to established monikers) is required. 

2. The definition of Against UnitedHealth or US Healthcare Insurance companies: 
    - Expresses disapproval, criticism, or opposition to UnitedHealth or US Healthcare Insurance companies 
    - Highlights perceived failures, negative consequences, or harmful outcomes of UnitedHealth or US Healthcare Insurance companies 
    - Clear demonstration of negative stance against UnitedHealth or US Healthcare Insurance companies is required. 

3. The definition of Neutral to UnitedHealth or US Healthcare Insurance companies: 
    - Presents mixed or conflicting stance, balancing both in favor and against aspects without leaning toward either side. 
    - Discusses topics unrelated to UnitedHealth or US Healthcare Insurance companies 
    - Does not mention or reference UnitedHealth or US Healthcare Insurance companies. 
    - Mentions United or Health but it is clear it is not talking about UnitedHealth or US Healthcare Insurance companies 
    - UnitedHealth or a US Healthcare Insurance company is mentioned but the stance is unclear. 
    - May include In-Favor or Against only based on extended contextual knowledge. 
    - Reference to objective reporting relating to UnitedHealth or a US Healthcare Insurance company (e.g. “United Health released a statement.”). 

4. Some posts might include multiple stances. Please focus on the overall stance toward Brian Thompson and choose the most dominant stance. 

# Examples 
    ## In-Favor Post: 
        “I can’t recommend UHC enough! Their policies were a lifesaver last year when I needed emergency surgery!” 
        “Insurance might be expensive, but you know what's more expensive? Paying out of pocket when an accident occurs. Everyone likes to talk big saying they don’t like insurance, but when an accident happens it's the first thing they go running for! I’m with UHC, protect our CEOS!!!” 
        “I think that health insurance companies have our best interest in mind, UnitedHealth specifically really helped me out when times were tough. Always grateful for my representative Melinda ❤️” 
        “Insurance companies do their best to provide excellent service to their customers, with a range of plans, I feel like their plan fits my needs” 

    ## Against Post: 
        “Luigi Mangione, you’re a hero. Fuck this system. Fuck Brian Thompson. Fuck this healthcare system.” 
        “Obama is responsible for the state of healthcare. Obama handed these insurance companies the power to be in charge of our health instead of doctors. We need to get back to competitive isurance across state lines! @realDonaldTrump” 
        “RT @JPo1369 In 2023, UnitedHealthcare dismissed one in every three claims. UHC and other companies use AI to evaluate claims. UHC and Humana have been sued over this practice. Do they really care? Probably not. Look at their profits below. Is UHC trying to be the Blackrock of…” 
        “They sure did, in every way possible. Also, I wouldn't say this murder was "coldblooded." Coldblooded is denying cancer patients care so you can buy a second home. Fuck Brian Thompson. Fuck privatizing healthcare. Fuck all of the greedy people...and fuck Elon Musk twice.” 

    ## Neutral Posts: 
        “RT @RashidKhan1515 @kaitlancollins This incident has shocked those familiar with Thompson's career, marking a somber moment not only for UnitedHealthcare but for the broader business community, given his prominent role in the healthcare industry.” 
        “@dvassallo Yes, however, UnitedHealthcare has almost twice as high net margin (6.11%) versus the industry average (3.4%). They have the lowest claim approvals out of any major healthcare company. Their business is not all insurance, they also invest in real estate and own the pharmacies” 
        “@FreedomMatter14 5.) Corporate Rivalry: Competition in Healthcare: The health insurance industry is highly competitive. While not directly linked to Thompson, the aggressive business environment might lead to extreme actions by competitors or those impacted adversely by UnitedHealthcare's market…” 
        “RT @Teh_Snowflake The healthcare industry isn’t “poorly designed.” It’s working as intended. https://t.co/zgBJKVxx4K https://t.co/CuvrNVv0F0” 

Now Classify the stance regarding UnitedHealth or US Healthcare Insurance companies in the following X post. Using the STANCE_DICT, output the numeric key for the stance 

{text}

# FORMATTING:
1. Please only provide a label for each post (1, -1, or 0).
2. Do not include any additional information or context.
3. You will be given a great penalty if you provide redundant information or context.
"""
}

def get_system_prompt(prompt_name=None):
    """Get system prompt by name"""
    from config import CONFIG
    if prompt_name is None:
        prompt_name = CONFIG.get('SYSTEM_PROMPT_NAME')
    return SYSTEM_PROMPTS.get(prompt_name, '')

def get_task_prompt(prompt_name=None):
    """Get task prompt by name"""
    from config import CONFIG
    if prompt_name is None:
        prompt_name = CONFIG.get('TASK_PROMPT_NAME')
    return TASK_PROMPTS.get(prompt_name, '')