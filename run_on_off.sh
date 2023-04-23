python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 0.3     --s_frac 1.0     --tr_frac 0.8     --seed 12345    --load_frac=0.25
echo "Done Data Gen"
python run_experiment_on_off.py 'alpha_0.3/'
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 0.4     --s_frac 1.0     --tr_frac 0.8 --seed 12345    --load_frac=0.25
echo "Done Data Gen"
python run_experiment_on_off.py 'alpha_0.4/'
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 0.8     --s_frac 1.0     --tr_frac 0.8 --seed 12345    --load_frac=0.25
echo "Done Data Gen"
python run_experiment_on_off.py 'alpha_0.8/'
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 2     --s_frac 1.0     --tr_frac 0.8 --seed 12345    --load_frac=0.25
echo "Done Data Gen"
python run_experiment_on_off.py 'alpha_2/'
python data/celeba/generate_data.py     --n_tasks 80     --n_components 3     --alpha 4     --s_frac 1.0     --tr_frac 0.8 --seed 12345    --load_frac=0.25
echo "Done Data Gen"
python run_experiment_on_off.py 'alpha_4/'
