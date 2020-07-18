from model.trainer.fsl_trainer import FSLTrainer
from model.utils import (
    pprint, set_gpu,
    get_command_line_parser,
    postprocess_args,
)
# from ipdb import launch_ipdb_on_exception

if __name__ == '__main__':
    parser = get_command_line_parser()
    args = parser.parse_args()
    args.eval = True
    args = postprocess_args(args)
    # with launch_ipdb_on_exception():
    pprint(vars(args))

    set_gpu(args.gpu)
    trainer = FSLTrainer(args)
    # trainer.train()
    trainer.evaluate_test(path=args.path)
    # trainer.final_record()
    print(args.save_path)