from ..base_atari_env import BaseAtariEnv, base_env_wrapper_fn


def raw_env(**kwargs):
    return BaseAtariEnv(game="space_invaders", num_players=2, mode_num=50, **kwargs)


env = base_env_wrapper_fn(raw_env)
