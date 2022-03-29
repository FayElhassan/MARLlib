from ray import tune


def run_pg_a2c_a3c(args, common_config, env_config, stop):
    config = {
        "env": args.map,
        "horizon": args.horizon,
        "model": {
            "custom_model": args.neural_arch,
        },
    }

    config.update(common_config)
    results = tune.run(args.run,
                       name=args.run + "_" + args.neural_arch + "_" + args.map,
                       stop=stop,
                       config=config,
                       verbose=1)

    return results