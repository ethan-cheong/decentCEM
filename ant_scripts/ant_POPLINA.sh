#!/bin/bash
# The following script will run POPLIN-A on pendulum

python mbexp.py \
    -env gym_ant \
    -logdir log/poplina \
    -o exp_cfg.exp_cfg.ntrain_iters 2 \
    -o exp_cfg.exp_cfg.ninit_rollouts 0 \
    -o exp_cfg.sim_cfg.task_hor 200 \
    -o ctrl_cfg.cem_cfg.cem_type POPLINA-INIT \
    -o ctrl_cfg.cem_cfg.training_scheme BC-AR \
    -o ctrl_cfg.cem_cfg.test_policy 1 \
    -o ctrl_cfg.cem_cfg.test_policy_epochs 1 \
    -o ctrl_cfg.cem_cfg.eval_ctrl_type MPC \
    -o ctrl_cfg.cem_cfg.debug_optimizer False \
    -ca model-type PE \
    -ca prop-type E \
    -ca opt-type POPLIN-A
