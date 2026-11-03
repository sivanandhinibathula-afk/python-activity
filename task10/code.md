
1. Problem Statement
Develop a Python program for campus event financial planning to calculate the total expenses involved in organizing an event, including venue charges, equipment costs, catering expenses, transportation costs, and certificate costs. The program determines the participant contribution amount, calculates sponsorship shortfalls, and identifies the minimum number of registrations required to break even. Finally, it displays a complete financial report indicating whether the event budget is sufficient.
2. Algorithm
1. Start the program.
2. Enter the event name.
3. Enter venue cost.
4. Enter equipment cost.
5. Enter catering cost per participant.
6. Enter transportation cost.
7. Enter certificate cost per participant.
8. Enter the expected number of participants.
9. Enter the sponsorship amount.
10. Calculate total fixed costs (venue, equipment, and transportation).
11. Calculate variable costs (catering and certificates).
12. Calculate the total event cost.
13. Calculate the sponsorship shortfall, if any.
14. Calculate the amount to be contributed by participants.
15. Calculate the contribution required per participant.
16. Calculate the minimum registration count required to break even.
17. Display the complete financial report.
18. Stop the program.



3. Flowchart – Mermaid Code




<img width="1080" height="1564" alt="image" src="https://github.com/user-attachments/assets/39118a9b-79d6-4dc1-97fa-27a1a5a52b72" />




1. Enter transportation cost.
2. Enter certificate cost per participant.
3. Enter the expected number of participants.
4. Enter the sponsorship amount.
5. Calculate total fixed costs (venue, equipment, and transportation).
6. Calculate variable costs (catering and certificates).
7. Calculate the total event cost.
8. Calculate the sponsorship shortfall, if any.
9. Calculate the amount to be contributed by participants.
10. Calculate the contribution required per participant.
11. Calculate the minimum registration count required to break even.
12. Display the complete financial report.
13. Stop the program.
3. Flowchart – Mermaid Code
Copy this code into Mermaid Live Editor.
#chatgpt-mermaid-_r_f3_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_f3_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_f3_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_f3_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-_r_f3_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_f3_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_f3_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_f3_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_f3_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_f3_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_f3_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_f3_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_f3_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_f3_ p{margin:0;}#chatgpt-mermaid-_r_f3_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_f3_ .label text,#chatgpt-mermaid-_r_f3_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ .node rect,#chatgpt-mermaid-_r_f3_ .node circle,#chatgpt-mermaid-_r_f3_ .node ellipse,#chatgpt-mermaid-_r_f3_ .node polygon,#chatgpt-mermaid-_r_f3_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_f3_ .rough-node .label text,#chatgpt-mermaid-_r_f3_ .node .label text,#chatgpt-mermaid-_r_f3_ .image-shape .label,#chatgpt-mermaid-_r_f3_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_f3_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_f3_ .rough-node .label,#chatgpt-mermaid-_r_f3_ .node .label,#chatgpt-mermaid-_r_f3_ .image-shape .label,#chatgpt-mermaid-_r_f3_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_f3_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_f3_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_f3_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-_r_f3_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-_r_f3_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-_r_f3_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_f3_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-_r_f3_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_f3_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-_r_f3_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-_r_f3_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_f3_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_f3_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_f3_ .icon-shape,#chatgpt-mermaid-_r_f3_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_f3_ .icon-shape p,#chatgpt-mermaid-_r_f3_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-_r_f3_ .icon-shape .label rect,#chatgpt-mermaid-_r_f3_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_f3_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_f3_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_f3_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_f3_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_f3_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_f3_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_f3_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_f3_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_f3_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_f3_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_f3_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_f3_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_f3_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_f3_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_f3_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_f3_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_f3_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_f3_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_f3_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_f3_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_f3_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_f3_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_f3_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_f3_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_f3_ .node rect,#chatgpt-mermaid-_r_f3_ .node circle,#chatgpt-mermaid-_r_f3_ .node ellipse,#chatgpt-mermaid-_r_f3_ .node polygon,#chatgpt-mermaid-_r_f3_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_f3_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_f3_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_f3_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_f3_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_f3_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter event nameEnter venue equipment andtransport costsEnter catering and certificatecostsEnter expected participantsEnter sponsorship amountEnter registration fee perparticipantCalculate fixed costsCalculate variable cost perparticipantCalculate total event costCalculate sponsorship shortfallCalculate total participantcontributionsRegistration fee greater thanvariable cost?Calculate minimum break-evenregistrationsCheck whether sponsorshipcovers fixed costsBreak-even possible with zeroregistrationsBreak-even not possibleDisplay financial reportStopYesNoYesNo





4. Source Code (Python)
import math# Campus Event Financial Planningevent = input("Enter event name: ")venue = float(input("Enter venue cost: "))equipment = float(input("Enter equipment cost: "))transport = float(input("Enter transport cost: "))catering = float(input("Enter catering cost per participant: "))certificate = float(input("Enter certificate cost per participant: "))participants = int(input("Enter expected number of participants: "))sponsorship = float(input("Enter sponsorship amount: "))registration_fee = float(input("Enter registration fee per participant: "))# Calculate fixed costsfixed_cost = venue + equipment + transport# Calculate variable cost per participantvariable_cost = catering + certificate# Calculate total variable costtotal_variable = variable_cost * participants# Calculate total event costtotal_cost = fixed_cost + total_variable# Calculate sponsorship shortfallsponsorship_shortfall = max(0, total_cost - sponsorship)# Calculate participant contributionsparticipant_contribution = registration_fee * participants



5. Source Input
Enter event name: Tech Fest

Enter venue cost: 10000
Enter equipment cost: 5000
Enter transport cost: 3000

Enter catering cost per participant: 200
Enter certificate cost per participant: 50

Enter expected number of participants: 100

Enter sponsorship amount: 15000
Enter registration fee per participant: 300


6. Source Output
===== CAMPUS EVENT FINANCIAL REPORT =====

Event Name: Tech Fest
Venue Cost: 10000.0
Equipment Cost: 5000.0
Transport Cost: 3000.0
Catering Cost: 20000.0
Certificate Cost: 2500.0

-----------------------------------------
Fixed Cost: 18000.0
Variable Cost: 25000.0
Total Event Cost: 43000.0

Sponsorship Amount: 15000.0
Sponsorship Shortfall: 28000.0

Expected Participants: 100
Registration Fee: 300.0
Total Participant Contributions: 30000.0

Total Income: 45000.0
Surplus / Deficit: 2000.0

Minimum Break-even Registrations: 60

Status: Event budget is sufficient
=========================================


7. Result
Thus, the Python program for Campus Event Financial Planning is successfully executed. It calculates venue, equipment, catering, transportation, and certificate costs, determines participant contributions and sponsorship shortfalls, and identifies the minimum number of registrations required to break even.









