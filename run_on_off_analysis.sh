printf "alpha_0.3\n" >> out_on_off.txt 
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 0.3     --s_frac 1.0     --tr_frac 0.8     --seed 12345    --load_frac=0.25
python celeba_transfer_attack_analysis_on_off.py 'alpha_0.3/' >> out_on_off.txt
printf "alpha_0.4\n" >> out_on_off.txt 
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 0.4     --s_frac 1.0     --tr_frac 0.8     --seed 12345    --load_frac=0.25
python celeba_transfer_attack_analysis_on_off.py 'alpha_0.4/' >> out_on_off.txt
printf "alpha_0.8\n" >> out_on_off.txt 
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 0.8     --s_frac 1.0     --tr_frac 0.8     --seed 12345    --load_frac=0.25
python celeba_transfer_attack_analysis_on_off.py 'alpha_0.8/' >> out_on_off.txt
printf "alpha_2\n" >> out_on_off.txt 
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 2     --s_frac 1.0     --tr_frac 0.8     --seed 12345    --load_frac=0.25
python celeba_transfer_attack_analysis_on_off.py 'alpha_2/' >> out_on_off.txt
printf "alpha_4\n" >> out_on_off.txt 
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 4     --s_frac 1.0     --tr_frac 0.8     --seed 12345    --load_frac=0.25
python celeba_transfer_attack_analysis_on_off.py 'alpha_4/'>> out_on_off.txt